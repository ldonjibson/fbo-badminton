from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .utils import *
import json

# Create your views here.

def my_team(request, message=False):
	print(request.user.teams)
	user = request.user
	context = {}
	user_team = Teams.objects.filter(owner=user).first()
	context['MSplayers'] = MSPlayer.objects.filter(team=user_team)
	context['WSplayers'] = WSPlayer.objects.filter(team=user_team)
	context['WDplayers'] = WDPlayer.objects.filter(team=user_team)
	context['MDplayers'] = MDPlayer.objects.filter(team=user_team)
	context['XDplayers'] = XDPlayer.objects.filter(team=user_team)
	context['team'] = user_team
	if message:
		messages.success(request, ("Successfully saved your team"))
	return render(request, 'authenticate/my_team.html', context)


def team_detail(request, team_pk):
	context = {}
	team = Teams.objects.get(pk=team_pk)
	context['MSplayers'] = MSPlayer.objects.filter(team=team)
	context['WSplayers'] = WSPlayer.objects.filter(team=team)
	context['WDplayers'] = WDPlayer.objects.filter(team=team)
	context['MDplayers'] = MDPlayer.objects.filter(team=team)
	context['XDplayers'] = XDPlayer.objects.filter(team=team)
	context['teampoints'] = team.get_team_total_points()
	return render(request, 'authenticate/team_detail.html', context)


def buy_players_index(request):
	user_team = Teams.objects.filter(owner=request.user).first()
	context = {}
	context['MSplayers_user'] = MSPlayer.objects.filter(team=user_team)
	context['WSplayers_user'] = WSPlayer.objects.filter(team=user_team)
	context['WDplayers_user'] = WDPlayer.objects.filter(team=user_team)
	context['MDplayers_user'] = MDPlayer.objects.filter(team=user_team)
	context['XDplayers_user'] = XDPlayer.objects.filter(team=user_team)
	context['MSplayers'] = list(MSPlayer.objects.all())
	context['WSplayers'] = list(WSPlayer.objects.all())
	context['WDplayers'] = list(WDPlayer.objects.all())
	context['MDplayers'] = list(MDPlayer.objects.all())
	context['XDplayers'] = list(XDPlayer.objects.all())
	context['team'] = user_team
	players_data_for_js = {}
	players_data_for_js['MS'] = len(MSPlayer.objects.filter(team=user_team))
	players_data_for_js['WS'] = len(WSPlayer.objects.filter(team=user_team))
	players_data_for_js['WD'] = len(WDPlayer.objects.filter(team=user_team))
	players_data_for_js['MD'] = len(MDPlayer.objects.filter(team=user_team))
	players_data_for_js['XD'] = len(XDPlayer.objects.filter(team=user_team))
	context['data'] = json.dumps(players_data_for_js)
	return render(request, 'authenticate/vacant_players.html', context)


def process_cart(request):
    user = request.user
    user_team = Teams.objects.filter(owner=user).first()
    players_to_sell = json.loads(request.POST.get('sell'))
    players_to_buy = json.loads(request.POST.get('buy'))
    print(players_to_sell, players_to_buy)
    if players_to_buy and players_to_sell:
        pass
    if players_to_buy:
        players = []
        for key in players_to_buy.keys():
            if players_to_buy[key]:
                type = key[:2]
                id = int(key[2:])
                players.append(get_player(type, id))

        if user_team.budget < sum([x.cost for x in players]):
            messages.success(request, ("You don't have enough funds"))
            return redirect('players-urls:buy_players')
        if user_team.get_team_value() + sum([x.cost for x in players]) > 120:
            messages.success(request, ("Your team's cost can't exceed 120"))
            return redirect('players-urls:buy_players')

        for player in players:
            if check_team_for_slots(request.user, player):
                message = check_team_for_slots(request.user, player)
                messages.success(request, message)
                return redirect('players-urls:buy_players')
            else:
                buy_player(request, player)

    if players_to_sell:
        for key in players_to_sell.keys():
            if players_to_sell[key]:
                type = key[:2]
                id = int(key[3:])
                player = get_player(type, id)
                sell_player(request, player)

    return my_team(request, message=True)


def player_profile(request, type, pk):
	profile = get_player(type, pk)
	return render(request, 'authenticate/player_profile.html', {'profile': profile})

