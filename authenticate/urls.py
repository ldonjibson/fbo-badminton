from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
	path('', views.home, name="home"),
	path('leaderboard/', views.leaderboard, name='leaderboard'),
	path('rules/', views.rules_page, name='rules'),
	path('fantasy_player_ranking/', views.fantasy_player_ranking, name='fantasy_player_ranking'),
	path('news/', views.news, name='news'),
	path('article/<slug>', views.article_detail, name='article_detail'),
	path('transfers/players', views.transfers, name='transfers'),
	# path('players/<player_type>/buy/<player_pk>', views.buy_player, name='buy_player'),
	path('data_upload/', views.data_upload, name='data_upload'), #for easy data upload

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
