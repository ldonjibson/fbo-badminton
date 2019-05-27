from django.contrib import admin
from django.urls import path, include
import mysite.views as views
from players.urls import urlpatterns as player_urls
from authenticate.urls import urlpatterns as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authenticate.urls', namespace='main-urls')),
    path('credit/', include('players.urls', namespace='players-urls')),
    path('csv_upload/', views.upload_csv, name='upload-csv'),
      
]
