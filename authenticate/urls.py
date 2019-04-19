from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.home, name="home"),
	path('my_team/', views.my_team, name='my_team'),
	path('leaderboard/', views.leaderboard, name='leaderboard'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
	path('change_password/', views.change_password, name='change_password'),
	path('rules/', views.rules_page, name='rules'),
	path('fantasy_player_ranking/', views.fantasy_player_ranking, name='fantasy_player_ranking'),
	path('news/', views.news, name='news'),
	path('article/<slug>', views.article_detail, name='article_detail'),
	path('transfers/players', views.transfers, name='transfers'),
	path('players/buy_list', views.buy_players_index, name='buy_players'),
	# path('players/<player_type>/buy/<player_pk>', views.buy_player, name='buy_player'),
    path('players/buy', views.process_cart, name='buy_bulk'),
	path('player/<player>', views.player_profile, name='player_profile'),
	path('teams/<team_pk>', views.team_detail, name='team_detail'),
	path('my_team/delete/<player_type>/<player_pk>', views.sell_player, name='sell_player'),
	path('my_team/create_league', views.LeagueCreate.as_view(), name='create_league'),
	path('my_team/update_league/<pk>', views.LeagueUpdate.as_view(), name='update_league'),
	path('my_team/delete_league/<pk>', views.LeagueDelete.as_view(), name='delete_league'),
	path('my_team/join_league', views.join_league, name='join_league'),
	path('my_team/league_list', views.LeagueList.as_view(), name='league_list'),
	path('my_team/league_list/<pk>', views.LeagueDetailView.as_view(), name='league_detail'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
