'''
Created on 2Nov.,2016

@author: GRDIEZ
'''
from __future__ import unicode_literals

from django.db import models
import Gamecore

# Create your models here.

class Player(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=120)
    last_name = models.CharField(verbose_name='Second Name',max_length=120)
    nickname = models.CharField(primary_key=True,verbose_name='Gamecore User Name',max_length=120, default='')
    email = models.CharField(verbose_name='Email',max_length=120)
    telephone = models.CharField(verbose_name='Telephone Number',max_length=120, default='')
    password_first = models.CharField(verbose_name='Password',max_length=120)
    password_second = models.CharField(verbose_name='Password confirmation',max_length=120)
    company = models.CharField(verbose_name='Company Name',max_length=120)
    city = models.CharField(verbose_name='City where you live',max_length=120, default='')
    flag_playstation = models.BooleanField(verbose_name='Do you play in Playstation?  ',default=False)
    flag_xbox = models.BooleanField(verbose_name='Do you play in Xbox?  ',default=False)
    flag_pc = models.BooleanField(verbose_name='Do you play in PC?  ',default=False)
    playstation_id = models.CharField(verbose_name='PlayStation ID',max_length=120, default='')
    welcoming_message = models.CharField(max_length=1200, default='Welcome to the game! Tell us your availability and your networking interests and we will set up the right games for you!')
    available = models.CharField(verbose_name='Update your availability for the next days/weeks',max_length=300, default='')
    
    
    def __str__(self):
        return self.nickname
    
    
    
class Match(models.Model):
    player1 = models.ForeignKey(Player, related_name='player1')
    player2 = models.ForeignKey(Player, related_name='player2', default ='') 
    timeDate = models.CharField(verbose_name='Match date',max_length=120)
    Game = models.CharField(verbose_name='Game',max_length=120)
    Score = models.CharField(verbose_name='Result of the Match',max_length=120, null=True)
    
class Ladder(models.Model):#Everytime we fill up a new score (Match) on the DB we need to generate to registers in the Ladder table
    player_id = models.ForeignKey(Player) 
    match_id = models.ForeignKey(Match) 
    points = models.IntegerField(null=True, default=0, verbose_name='Points')
    flag_win = models.IntegerField(null=True, default=0, verbose_name='Winds')
    flag_draw = models.IntegerField(null=True, default=0, verbose_name='Draws')
    flag_loss = models.IntegerField(null=True, default=0, verbose_name='Losses')
    goals_scored = models.IntegerField(null=True, default=0, verbose_name='Goals scored')
    goals_received = models.IntegerField(null=True, default=0, verbose_name='Goals received')
    total_shots = models.IntegerField(null=True, default=0, verbose_name='Total shots')
    shots_target = models.IntegerField(null=True, default=0, verbose_name='Shots on target')
    possession = models.FloatField(null=True, default=0.0, verbose_name='possession')        

class ContactUs(models.Model):
    first_name = models.CharField(verbose_name='First name',max_length=120)
    last_name = models.CharField(verbose_name='Last name',max_length=120)
    email = models.CharField(verbose_name='Email address',max_length=120)
    subject = models.CharField(verbose_name='Subject',max_length=120)
    message = models.CharField(verbose_name='Message',max_length=1200)
    time = models.DateTimeField(auto_now=True)

class LogIn(models.Model):
    nickname = models.CharField(max_length=120, default='')
    password = models.CharField(max_length=120, default='')
    loginTime = models.DateTimeField(auto_now=True)
    
class SuggestedLeague(models.Model):
    game = models.CharField(max_length=120, default='')
    platform = models.CharField(max_length=120, default='')
    user_nickname = models.ForeignKey(Player) 
    time = models.DateTimeField(auto_now=True)
    
#class PlayerAvailability(models.Model):
#    player_id = models.ForeignKey(Player)
 #   available = models.CharField(verbose_name='Update your availability for the next days/weeks',max_length=300)

  #  def __str__(self):
   #     return self.title   
