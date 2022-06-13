from django.contrib import admin
from django.urls import path, include
from inbox import views

urlpatterns = [

    path('', views.inbox, name='inbox'),

]