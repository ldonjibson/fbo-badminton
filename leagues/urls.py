from django.urls import path
from . import views

app_name = 'leagues'

urlpatterns = [
    path('my_team/create_league', views.LeagueCreate.as_view(), name='create_league'),
    path('my_team/update_league/<pk>', views.LeagueUpdate.as_view(), name='update_league'),
    path('my_team/delete_league/<pk>', views.league_delete, name='delete_league'),
    path('my_team/join_league', views.join_league, name='join_league'),
    path('my_team/league_list', views.LeagueList.as_view(), name='league_list'),
    path('my_team/league_list/<pk>', views.LeagueDetailView.as_view(), name='league_detail'),

]