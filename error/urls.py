from django.contrib import admin
from django.urls import path, include
from error import views

urlpatterns = [

    path('', views.error, name='error'),

]
