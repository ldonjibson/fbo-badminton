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
	path('transfers/', views.transfers, name='transfers'),
	path('<player>/', views.player_profile, name='player_profile'),
	path('<slug>/', views.article_detail, name='article_detail'),
	path('<team>/', views.team_detail, name='team_detail'),




]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
