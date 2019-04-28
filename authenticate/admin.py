from django.contrib import admin
from .models import *
from players.models import *

admin.site.register(MSPlayer)
admin.site.register(WDPlayer)
admin.site.register(MDPlayer)
admin.site.register(WSPlayer)
admin.site.register(XDPlayer)
admin.site.register(Article)
admin.site.register(Teams)