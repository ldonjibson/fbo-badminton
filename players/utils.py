from .models import *


def get_all_players():
	all = 0
	for player_type in Player.__subclasses__():
		if not all:
			all = player_type.objects.all()
		all = all.union(player_type.objects.all())
	return all

def get_player(player_type, player_pk):
    if player_type == 'MS':
        player = MSPlayer.objects.get(pk=player_pk)
    elif player_type == 'WS':
        player = WSPlayer.objects.get(pk=player_pk)
    elif player_type == 'MD':
        player = MDPlayer.objects.get(pk=player_pk)
    elif player_type == 'WD':
        player = WDPlayer.objects.get(pk=player_pk)
    else:
        player = XDPlayer.objects.get(pk=player_pk)
    return player

def check_team_for_slots(user, player):
    player_type = player.get_type()
    user_team = Teams.objects.filter(owner = user).first()
    if player_type == 'MS':
        if len(user_team.MSplayers.all()) < 2:
            return False
        else:
            return "Not enough MS Slots"
    elif player_type == 'WS':
        if len(user_team.WSplayers.all()) < 2:
            return False
        else:
            return "Not enough WS Slots"
    elif player_type == 'MD':
        if len(user_team.MDplayers.all()) < 2:
            return False
        else:
            return "Not enough MD Slots"
    elif player_type == 'WD':
        if len(user_team.WDplayers.all()) < 2:
            return False
        else:
            return "Not enough WD Slots"
    else:
        if len(user_team.XDplayers.all()) < 2:
            return False
        else:
            return "Not enough XD Slots"


def sell_player(request, player):
    user = request.user
    user_team = Teams.objects.filter(owner = user).first()
    user_team.budget += player.cost
    user_team.save()
    player.team = None
    player.save()

def buy_player(request, player):
	user = request.user
	user_team = Teams.objects.filter(owner=user).first()
	user_team.budget -= player.cost
	user_team.save()
	player.team = user_team
	player.save()