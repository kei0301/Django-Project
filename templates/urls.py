from django.contrib import admin
from django.urls import path, include
from templates import views

urlpatterns = [

    path('', views.templates, name='templates'),
    path('add/', views.templates_add, name='templates_add'),
    path('detail/<id>', views.templates_detail, name='templates_detail'),
    path('generate/', views.templates_generate, name='templates_generate'),

    path('domains/', views.domains, name='templates_domains'),
    path('domains/add/', views.domains_add, name='templates_domains_add'),
    path('domains/verify/', views.domains_verify,
         name='templates_domains_verify'),

    path('files/', views.files, name='templates_files'),
    path('files/add/', views.files_add, name='templates_files_add'),

    path('folders/', views.folders, name='templates_folders'),
    path('folders/add/', views.folders_add, name='templates_folders_add'),

    path('plans/', views.plans, name='plans'),
    path('plans/checkout/', views.plans_checkout, name='plans_checkout'),
    path('plans/checkout/failed/', views.plans_checkout_failed,
         name='plans_checkout_failed'),
    path('plans/checkout/passed/', views.plans_checkout_passed,
         name='plans_checkout_passed'),

    path('settings/', views.settings, name='settings'),

]
