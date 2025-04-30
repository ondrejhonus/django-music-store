from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('strings/', views.strings, name='strings'),
    path('strings/<str:type>/', views.string_type, name='strings'),
    path('percussion/', views.percussion, name='percussion'),
    path('percussion/<str:type>/', views.percussion_type, name='percussion'),
    path('keyboards/', views.keyboards, name='keyboards'),
    path('keyboards/<str:type>/', views.keyboard_type, name='keyboards'),
    path('wind-instruments/', views.wind, name='wind'),
    path('wind-instruments/<str:type>/', views.wind_type, name='wind-instruments'),
]
