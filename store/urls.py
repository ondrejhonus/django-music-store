from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('strings/', views.strings, name='strings'),
    path('percussion/', views.percussion, name='percussion'),
    path('keyboards/', views.keyboards, name='keyboards'),
    path('wind-instruments/', views.wind, name='wind'),
]
