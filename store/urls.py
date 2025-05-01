from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instruments/<slug:cat>/<slug:slug>/', views.instrument_detail, name='instrument_detail'),
    # path('strings/', views.strings, name='strings'),
    # path('strings/<slug:type>/', views.string_type, name='strings'),
    # path('percussion/', views.percussion, name='percussion'),
    # path('percussion/<slug:type>/', views.percussion_type, name='percussion'),
    # path('keyboards/', views.keyboards, name='keyboards'),
    # path('keyboards/<slug:type>/', views.keyboard_type, name='keyboards'),
    # path('wind-instruments/', views.wind, name='wind'),
    # path('wind-instruments/<slug:type>/', views.wind_type, name='wind-instruments'),
    path('<slug:category_slug>/<slug:type_slug>/', views.instrument_type, name='instrument_type'),
    path('<slug:category_slug>/', views.instrument, name='instrument'),
]
