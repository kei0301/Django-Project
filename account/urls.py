from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [

    path('', views.account, name='account'),
    path('thread/', views.thread, name='thread'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('reset/', views.reset, name='reset'),
    path('change/', views.change, name='change'),

    path('register/thanks/', views.thanks, name='thanks'),

    path('settings/', views.settings, name='settings'),
    path('update/', views.update, name='update'),
    path('invite/', views.invite, name='invite'),

]
