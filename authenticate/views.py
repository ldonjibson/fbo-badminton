from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages

from players.utils import get_all_players, Team
from .models import *
import json
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.crypto import get_random_string
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
import csv, io




def home(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'home.html', {'articles': articles})

def leaderboard(request):
	all_teams = Team.objects.all().order_by('-points')
	return render(request, 'authenticate/leaderboard.html', {'all_teams': all_teams})

def rules_page(request):
	return render(request, 'authenticate/rules_page.html', {})



def fantasy_player_ranking(request):
	all_ranking = get_all_players()
	return render(request, 'players/fantasy_player_ranking.html', {'all_ranking': all_ranking})



def news(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'authenticate/news.html', {'articles': articles})

def article_detail(request, slug):
	#return HttpResponse(slug)
	article = Article.objects.all()[0]
	return render(request, 'authenticate/article_detail.html', {'article': article})



def transfers(request):
	all_ranking = get_all_players()
	return render(request, 'players/transfers.html', {'all_ranking': all_ranking})










#for easy data upload
def data_upload(request):
	template = "data_upload.html"

	if request.method == "GET":
		return render(request, template)

	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'This is not a csv file')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, created = Data.objects.update_or_create(
		name=column[0],
		cost=column[1],
		form=column[2],
		career_winrate=column[3],
		year_winrate=column[4]
		)

	context = {}
	return render(request, template, context)





#attempt at api content for news page
	#import requests
	#import json
	#api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=99509d87cbcb4b81ababc39ca20d8175")
	#api = json.loads(api_request.content)
	#return render(request, 'authenticate/news.html', {'api' : api })
