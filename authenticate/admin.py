from django.contrib import admin
from .models import Ranking
from .models import Article
from .models import Teams

admin.site.register(Ranking)
admin.site.register(Article)
admin.site.register(Teams)