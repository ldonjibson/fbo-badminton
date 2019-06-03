from django.contrib import admin
from .models import *
from players.models import *




admin.site.register(Article)
admin.site.register(Team)

# admin.site.register(UserLeagueParticipation)