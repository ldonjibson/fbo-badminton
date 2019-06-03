from django.contrib import admin

# Register your models here.
from leagues.models import UserLeagueParticipation, League


class MemberInline(admin.TabularInline):
    model = UserLeagueParticipation

class LeagueAdmin(admin.ModelAdmin):
    inlines = (MemberInline,)

admin.site.register(League, LeagueAdmin)
