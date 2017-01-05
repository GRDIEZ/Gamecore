'''
Created on 2Nov.,2016

@author: GRDIEZ


'''
from django.conf.urls import url, include
from Gamecore_app import views
from django.contrib import admin

urlpatterns = [
   url(r'^$', views.Intro),
   url(r'signup/$', views.Signup, name='Signup'),
   url(r'account/$', views.Account, name='Account'),
   url(r'profile/$', views.Profile, name='Profile'),
   url(r'leagues/$', views.Leagues, name='Leagues'),
   url(r'upcominggames/$', views.UpcomingGames, name='UpcomingGames'),
   url(r'availability/$', views.Availability, name='Availability'),
   url(r'uploadresults/$', views.UploadResults, name='UploadResults'),
   url(r'about/$', views.About, name='About'),
   url(r'instructions/$', views.Instructions, name='Instructions'),
   url(r'contact/$', views.Contact, name='Contact'),

    
    ]