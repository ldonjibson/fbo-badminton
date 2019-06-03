from django.contrib import admin
from django.urls import path, include
from . import views
from .api.views import update_players, get_player_modal

app_name = 'players'

API_url_patters = [
    path('api/players-update', update_players, name='api-update-players'),
    path('api/player-update', get_player_modal, name='api-update-player-modal')
]

urlpatterns = [
    path('transfers', views.transfers, name='transfers'),
    path('buy_list', views.buy_players_index, name='buy_players'),
    path('buy', views.process_cart, name='buy_bulk'),
    path('teams/<team_pk>', views.team_detail, name='team_detail'),
    path('my_team/', views.my_team, name='my_team'),
    path('player/<type>-<pk>', views.player_profile, name='player_profile'),

] + API_url_patters
