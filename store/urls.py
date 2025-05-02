from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('instruments/<slug:cat>/<slug:slug>/', views.instrument_detail, name='instrument_detail'),
    path('instruments/<slug:cat>/delete/<slug:slug>/', views.instrument_delete, name='instrument_delete'),
    path('instruments/add/', views.instrument_create, name='instrument_create'),
    path('instruments/<slug:cat>/edit/<slug:slug>/', views.instrument_update, name='instrument_update'),
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
