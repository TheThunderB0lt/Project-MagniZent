from django.contrib import admin
from django.urls import path, include
from Master import views

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('team/', views.team_view, name='team'),
    path('contact/', views.contact_view, name='contact'),
]
