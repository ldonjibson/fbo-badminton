from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET
from django.template import loader, Context
from players.models import WSPlayer, XDPlayer, MSPlayer, MDPlayer, WDPlayer
from django.core.paginator import Paginator


@require_GET
def update_players(request):
    # since bootstrap provides its own pagination, for now it's okay to use it. Later, when it'll take too long to load
    # all the players in a single go, I'll uncomment the pagination code

    type = request.GET.get('type')
    players_list = eval(type+'Player.objects.all()')
    # posts_per_page = request.POST.get('players_per_page', 10)
    # page = request.POST.get('page', 1)
    # paginator = Paginator(players_list, posts_per_page)
    # players = paginator.get_page(page)
    t = loader.get_template('players/tranfers_table.html')
    rendered = t.render({'players': players_list})

    return JsonResponse(rendered, safe=False)


@require_GET
def get_player_modal(request):

    type = request.GET.get('type')
    id = request.GET.get('id')

    player = eval(type + 'Player.objects.filter(id={}).first()'.format(id))
    t = loader.get_template('players/modal/player.html')
    rendered = t.render({'player': player})

    return JsonResponse(rendered, safe=False)