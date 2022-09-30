#Project Library Management System
#---SANOJ KUMAR PRADHAN---#




#created this python file to make a list of urlpatterns and in each index stored path function,
#which routes the URLs to appropriate view functions

from django.contrib import admin
from django.urls import path
from lms import views    #imported views from app


urlpatterns = [
    path('', views.loginUser, name="home"),
    path('home',views.Home,name="home"),
    path('login',views.loginUser,name="login"),
    path('signup',views.AdminSignup,name="signup"),
    path('stuview',views.stuview,name="stuview"),
    path('admview',views.admview, name="admview"),
    path('updatebutton', views.updatebutton, name="updatebutton"),
    path('updatebook',views.updatebook,name="updatebook"),
    path('deletebook',views.deletebook,name="deletebook"),
    path('addbook',views.addbook,name="addbook"),
    path('addbutton',views.addbutton,name="addbutton"),
    path('logout',views.logoutUser,name="logout")
]