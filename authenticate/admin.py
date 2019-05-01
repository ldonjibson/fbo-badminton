from django.contrib import admin
from .models import *
from players.models import *

class MemberInline(admin.TabularInline):
    model = UserLeagueParticipation

class LeagueAdmin(admin.ModelAdmin):
    inlines = (MemberInline,)

admin.site.register(MSPlayer)
admin.site.register(WDPlayer)
admin.site.register(MDPlayer)
admin.site.register(WSPlayer)
admin.site.register(XDPlayer)
admin.site.register(Article)
admin.site.register(Teams)
admin.site.register(League, LeagueAdmin)
# admin.site.register(UserLeagueParticipation)