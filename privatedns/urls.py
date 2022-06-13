from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.routing, name='landings'),
    path('<slug>', views.paths, name='paths'),

]
