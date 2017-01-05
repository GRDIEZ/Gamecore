import Gamecore
import datetime
from django.contrib import messages
from django.db import connection
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, render_to_response
from django.http import HttpResponse
from .forms import PlayerForm, LogInForm, EditPlayerForm, ContactUsForm, AvailabilityForm, SuggestLeagueForm
from .models import Player, ContactUs#, PlayerAvailability
from Gamecore_app.models import Match, Ladder


def Intro(request):
    context = {   }
    return render(request, "index.html", context)

def Instructions(request):
    context = {   }
    return render(request, "instructions.html", context)

def Account(request):
    active_username = request.session.get('nickname', '')
    active_Player = Player.objects.get(nickname = active_username)
                
    context = {
        "nickname": active_username,
        "active_Player": active_Player
    }

    return render(request, "account.html", context)

def Profile(request):
    active_username = request.session.get('nickname', '')
    instance = get_object_or_404(Player, nickname=active_username)
    editing_player_form = EditPlayerForm(request.POST or None, instance=instance)
    message = ""
    
    if editing_player_form.is_valid(): 
        if (editing_player_form.cleaned_data.get("password_first") == editing_player_form.cleaned_data.get("password_second")):
            instance = editing_player_form.save(commit=False)
            #print(player_form.cleaned_data.get("first_name")) #prints in console
            
            instance.save() #saves in database
            #messages.success(request, "Successfully updated")
            message = "Successfully updated"
            
        else:
                #messages.success(request, "Not Successfully created")#WE NEED TO SHOW A POP UP TO THE USER
                message = "The update was not possible, review your input data"
            
    context = { 
        "instance": instance,
        "nickname": active_username,
        "editing_player_form":editing_player_form,
        "message": message
        }
    return render(request, "profile.html", context)


def Leagues(request):
    active_username = request.session.get('nickname', '')
    message =""
    
    if request.GET.get("rocket"):#IF THEY CLICKED THE ROCKET LEAGUE BUTTON
        cursor = connection.cursor()
        cursor.execute("INSERT INTO gamecore_app_suggestedleague (game, platform, user_nickname_id, time) values ('Rocket League','Playstation','"+ active_username + "' , '" + str(datetime.datetime.now()) + "')" )
        message =  "Thank you for the suggestion"
        
    if request.GET.get("battle"):#IF THEY CLICKED THE BATTLEFIELD BUTTON
        cursor = connection.cursor()
        cursor.execute("INSERT INTO gamecore_app_suggestedleague (game, platform, user_nickname_id, time) values ('Battlefield 1','Playstation','"+ active_username + "' , '" + str(datetime.datetime.now()) + "')" )
        message =  "Thank you for the suggestion"
        
    if request.GET.get("legends"):#IF THEY CLICKED THE LEAGUE OF LEGENDS BUTTON
        cursor = connection.cursor()
        cursor.execute("INSERT INTO gamecore_app_suggestedleague (game, platform, user_nickname_id, time) values ('League of legends','PC','"+ active_username + "' , '" + str(datetime.datetime.now()) + "')" )
        message =  "Thank you for the suggestion"
    
    suggestleague_form = SuggestLeagueForm(request.POST or None, initial={'user_nickname': active_username})
    if suggestleague_form.is_valid(): 
        instance = suggestleague_form.save(commit=False)
        instance.player_id = active_username
        instance.save() #saves in database
        #messages.success(request, "Thank you for the suggestion")
        suggestleague_form = SuggestLeagueForm(None, initial={'user_nickname': active_username})
        message =  "Thank you for the suggestion"
            
            
    #the following doesn't allow real group by
    #ladder_entries = Ladder.objects.raw('SELECT player_id_id, sum(points) , sum(flag_win) as wins, sum(flag_draw) as draws, sum(flag_loss) as losses, sum( goals_scored) as goals_scored, sum(goals_received), goals_received, sum(total_shots) as total_shots, sum(shots_target) as shots_target, avg(possession)*100 as possesion FROM gamecore_app_ladder group by player_id_id order by sum(points)')
    #the following allows group by:
    cursor = connection.cursor()
    cursor.execute("SELECT ld.player_id_id as player_id_id, company, sum(points) as points , sum(flag_win) as wins, sum(flag_draw) as draws, sum(flag_loss) as losses, sum( goals_scored) as goals_scored, sum(goals_received), goals_received, sum(total_shots) as total_shots, sum(shots_target) as shots_target, round(avg(possession),2) as possession FROM gamecore_app_ladder ld, gamecore_app_player pl where ld.player_id_id = pl.nickname group by ld.player_id_id, company order by sum(points) desc")
    results = cursor.fetchall()

    x = cursor.description
    resultsList = []   
    for r in results:
        i = 0
        d = {}
        while i < len(x):
            d[x[i][0]] = r[i]
            i = i+1
        resultsList.append(d)
        
    cursor = connection.cursor()
    cursor.execute("SELECT mt.id as id, mt.player1_id as player1, mt.player2_id as player2, pl1.company as company1, pl2.company as company2, timeDate, Game, Score FROM gamecore_app_player pl1, gamecore_app_match mt, gamecore_app_player pl2 where mt.player1_id = pl1.nickname and mt.player2_id = pl2.nickname ")
    results2 = cursor.fetchall()

    x = cursor.description
    resultsList2 = []   
    for r in results2:
        i = 0
        d = {}
        while i < len(x):
            d[x[i][0]] = r[i]
            i = i+1
        resultsList2.append(d)
            
    context = { 
        "nickname": active_username,
        "ladder_entries": resultsList,
        "fixture_entries": resultsList2,
        "suggestleague_form": suggestleague_form,
        "message": message
    }
    return render(request, "leagues.html", context)

def UpcomingGames(request):
    active_username = request.session.get('nickname', '')
    match_list = Match.objects.filter(player1__exact=active_username)

    context = {  
        "nickname": active_username,
        "match_list": match_list
        }
    
    return render(request, "upcominggames.html", context)

def Availability(request):
    active_username = request.session.get('nickname', '')
    
    #instance = get_object_or_404(PlayerAvailability, player_id_id=active_username)
    
    active_Player_availability = Player.objects.filter(nickname=active_username)
    
    if(active_Player_availability.first()):#we check if it not empty
        instance = get_object_or_404(Player, nickname=active_username)
        availability_form = AvailabilityForm(request.POST or None, instance=instance)        
    else:
        availability_form = AvailabilityForm(request.POST or None)
    
    #availability_form.player_id_id=active_username
    if availability_form.is_valid():
        instance = availability_form.save(commit=False)
        #instance.player_id = active_username
        instance.save(update_fields=['available']) #saves in database
        messages.success(request, "Successfully updated")
            
    #else:
        #messages.success(request, "Not Successfully created")#WE NEED TO SHOW A POP UP TO THE USER
        
    context = {  
        "nickname": active_username,
        "availability_form": availability_form
    }
    return render(request, "availability.html", context)

def UploadResults(request):
    
    active_username = request.session.get('nickname', '')
    
    context = { 
        "nickname": active_username,
    }
    
    return render(request, "uploadresults.html", context)

def Contact(request):
    contactUs_form = ContactUsForm(request.POST or None)
    active_username = request.session.get('nickname', '')
    instance = contactUs_form.save(commit=False)
    message = ""
    if contactUs_form.is_valid(): 
        instance = contactUs_form.save(commit=False)
        instance.save() #saves in database
        message = "Thank you for your comment"

    context = { 
        "instance": instance,
        "nickname": active_username,
        "contactUs_form":contactUs_form,
        "message": message
    }
    return render(request, "contact.html", context)

def About(request):
    active_username = request.session.get('nickname', '')
    context = {  
        "nickname": active_username,
    }
    return render(request, "about.html", context)


def Signup(request, active_username=None):
    
    if request.POST.get("sign_up"):
        player_form = PlayerForm(request.POST or None)
        if player_form.is_valid(): 
            if (player_form.cleaned_data.get("password_first") == player_form.cleaned_data.get("password_second")):
                instance = player_form.save(commit=False)
                #print(player_form.cleaned_data.get("first_name")) #prints in console
                
                instance.save() #saves in database
                #messages.success(request, "Successfully created")
                active_username = player_form.cleaned_data.get("nickname")
                request.session['nickname'] = active_username #we incorporate it on the session so we can use it across the views file
                active_Player = Player.objects.get(nickname = active_username)
                
                context = {
                    "instance": instance,
                    "nickname": active_username,
                    "active_Player": active_Player
                }
                #return render(request, "user_data.html", context)
                #WE HAVE TO UNLOCK THE MY ACCOUNT AREA
                return render(request, "account.html", context)
            else:
                #if request.POST.get("content")=="":
                    #messages.success(request, "Not Successfully created")#WE NEED TO SHOW A POP UP TO THE USER
                message = "Invalid Input data. Please, insert correct data and password"
                active_username= ""
                request.session['nickname'] = active_username #we incorporate it on the session so we can use it across the views file    
                player_form = PlayerForm(request.POST or None)
                login_form = LogInForm(request.POST or None)
                context = {
                    "message": message,
                    "nickname": active_username,
                    "player_form": player_form,
                    "login_form": login_form
                }
                #http://stackoverflow.com/questions/28240746/django-how-to-implement-alertpopup-message-after-complete-method-in-view
                return render(request, 'signup.html',context)
            
    else:
        if request.POST.get("sign_in"):#IF THEY CLICKED THE SIGN IN BUTTON THEN
            login_form = LogInForm(request.POST or None)
            if login_form.is_valid():
                active_username= login_form.cleaned_data.get("nickname")
                password_introduced = login_form.cleaned_data.get("password")
                
                # We have to validate that that user is already in the database
                active_Player = Player.objects.get(nickname = active_username)
                #TODO: LEARN TO CATCH THE 'DOESNOTEXIST' EXCEPTION AND SHOW A POP UP SAYING 'INCORRECT USER'
                if password_introduced == active_Player.password_first:
                    
                    instance = login_form.save(commit=False)
                    #print(player_form.cleaned_data.get("first_name")) #prints in console
                
                    instance.save() #saves in database
                    
                    match_list = Match.objects.filter(player1__exact=active_username)
                    #FILTER FOR GAMES WITH NO RESULTS       
                    
                    request.session['nickname'] = active_username #we incorporate it on the session so we can use it across the views file
                    
                    context = {
                     #"instance": instance,
                    "nickname": active_username,
                    "active_Player": active_Player,
                    "match_list": match_list
                    }
                    
                    #return render(request, "user_data.html", context)
                    #WE HAVE TO UNLOCK THE MY ACCOUNT AREA
                    return render(request, "account.html", context)
                
                else:
                    #LogInForm.clear TODO: empty the content of the form
                    #messages.success(request, "INVALID USER/PASSWORD")
                    
                    message = "INVALID USER/PASSWORD"
                    active_username= ""
                    request.session['nickname'] = active_username #we incorporate it on the session so we can use it across the views file
                    player_form = PlayerForm(None)
                    login_form = LogInForm(None)
                    context = {
                        "message": message,
                        "nickname": active_username,
                        "player_form": player_form,
                        "login_form": login_form
                    }
                    #POP UP SAYING THAT THE USER IS INCORRECT: http://stackoverflow.com/questions/28240746/django-how-to-implement-alertpopup-message-after-complete-method-in-view
                    return render(request, 'signup.html',context)
        #else:
    player_form = PlayerForm(None)
    login_form = LogInForm(None)
    context = {
        "nickname": active_username,
        "player_form": player_form,
        "login_form": login_form
    }
    return render(request, "signup.html", context)
 
 
