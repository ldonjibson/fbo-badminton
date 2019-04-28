from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'players'

urlpatterns = [
    path('buy_list', views.buy_players_index, name='buy_players'),
    path('buy', views.process_cart, name='buy_bulk'),
    path('teams/<team_pk>', views.team_detail, name='team_detail'),
    path('my_team/', views.my_team, name='my_team'),
    path('player/<type>-<pk>', views.player_profile, name='player_profile'),
]