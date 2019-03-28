from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from .models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'authenticate/home.html', {'articles': articles})

def leaderboard(request):
	all_teams = Teams.objects.all().order_by('-points')
	return render(request, 'authenticate/leaderboard.html', {'all_teams': all_teams})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Logged in!'))
			return redirect('home')

		else:
			messages.success(request, ('Error. Please try again'))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('Logged out!'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('Yay! You have registered'))
			return redirect('home')
	else:
		form = SignUpForm()

	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('Wohoo! You have successfully edited your profile'))
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('Nice! You have successfully edited your password'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)

def rules_page(request):
	return render(request, 'authenticate/rules_page.html', {})

def fantasy_player_ranking(request):
	all_ranking = Ranking.objects.all()
	return render(request, 'authenticate/fantasy_player_ranking.html', {'all_ranking': all_ranking })

def player_profile(request, player):
	profile = Ranking.objects.get(player=player)
	return render(request, 'authenticate/player_profile.html', {'profile': profile })

def news(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'authenticate/news.html', {'articles': articles})

def article_detail(request, slug):
	#return HttpResponse(slug)
	article = Article.objects.all()[0]
	return render(request, 'authenticate/article_detail.html', {'article': article})

def team_detail(request, team):
	return HttpResponse(team)
	#teambox = Teams.objects.get(team=team)
	return render(request, 'authenticate/team_detail.html', {'teambox': teambox})

def transfers(request):
	all_ranking = Ranking.objects.filter().order_by('-last')
	return render(request, 'authenticate/transfers.html', {'all_ranking': all_ranking })

def my_team(request):
	user = request.user
	context = {}
	user_team = Teams.objects.filter(owner=user).first()
	context['MSplayers'] = MSPlayer.objects.filter(team=user_team)
	context['WSplayers'] = WSPlayer.objects.filter(team=user_team)
	context['WDplayers'] = WDPlayer.objects.filter(team=user_team)
	context['MDplayers'] = MDPlayer.objects.filter(team=user_team)
	context['XDplayers'] = XDPlayer.objects.filter(team=user_team)
	context['team'] = user_team
	return render(request, 'authenticate/my_team.html', context)


def sell_player(request, player_pk, player_type):
	user = request.user
	user_team = Teams.objects.filter(owner=user).first()
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
	user_team.budget += player.cost
	user_team.save()
	player.team = None
	player.save()
	return redirect('my_team')


def buy_players_index(request):
	user_team = Teams.objects.filter(owner=request.user).first()
	context = {}
	context['players'] = list(MSPlayer.objects.filter(team=None))
	context['players'] += list(WSPlayer.objects.filter(team=None))
	context['players'] += list(WDPlayer.objects.filter(team=None))
	context['players'] += list(MDPlayer.objects.filter(team=None))
	context['players'] += list(XDPlayer.objects.filter(team=None))
	context['team'] = user_team
	return render(request, 'authenticate/vacant_players.html', context)


def buy_player(request, player_type, player_pk):
	user = request.user
	user_team = Teams.objects.filter(owner=user).first()
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
	user_team.budget -= player.cost
	user_team.save()
	player.team = user_team
	player.save()
	return redirect('buy_players')


#attempt at api content for news page
	#import requests
	#import json
	#api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=99509d87cbcb4b81ababc39ca20d8175")
	#api = json.loads(api_request.content)
	#return render(request, 'authenticate/news.html', {'api' : api })
