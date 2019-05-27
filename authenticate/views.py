from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages

from players.utils import get_all_players
from .forms import SignUpForm, EditProfileForm, KeyForm
from .models import *
import json
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.crypto import get_random_string
from authenticate.models import League
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q




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
			return redirect('main-urls:home')

		else:
			messages.success(request, ('Error. Please try again'))
			return redirect('main-urls:login')
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('Logged out!'))
	return redirect('main-urls:home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			Teams.objects.create(owner=user)
			login(request, user)
			messages.success(request, ('Yay! You have registered'))
			return redirect('main-urls:home')
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
			return redirect('main-urls:home')
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
			return redirect('main-urls:home')
	else:
		form = PasswordChangeForm(user=request.user)

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)

def rules_page(request):
	return render(request, 'authenticate/rules_page.html', {})



def fantasy_player_ranking(request):
	all_ranking = get_all_players()
	return render(request, 'authenticate/fantasy_player_ranking.html', {'all_ranking': all_ranking })



def news(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'authenticate/news.html', {'articles': articles})

def article_detail(request, slug):
	#return HttpResponse(slug)
	article = Article.objects.all()[0]
	return render(request, 'authenticate/article_detail.html', {'article': article})



def transfers(request):
	all_ranking = get_all_players()
	return render(request, 'authenticate/transfers.html', {'all_ranking': all_ranking })











class LeagueCreate(CreateView):
	model = League
	fields = ['name']
	success_url = reverse_lazy('players-urls:my_team')

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.owner = self.request.user
		obj.invite_key = get_random_string(length=32)
		obj.save()
		return super().form_valid(form)


class LeagueUpdate(UpdateView):
	model = League
	fields = ['name']
	success_url = reverse_lazy('players-urls:my_team')



def join_league(request):
	if request.method == 'POST':
		form = KeyForm(request.POST)
		if form.is_valid():
			user = request.user
			key = request.POST['key']
			league = League.objects.filter(invite_key=key).first()
			if league and not UserLeagueParticipation.objects.filter(user=user, league=league):
				UserLeagueParticipation.objects.create(user=user, league=league)
				messages.success(request, "Successfully joined league")
				return HttpResponseRedirect(reverse_lazy('players-urls:my_team'))
			elif UserLeagueParticipation.objects.filter(user=user, league=league):
				messages.success(request, "You are already a member of this league")
			else:
				messages.success(request, "League not found")
	else:
		form = KeyForm()

	return render(request, 'authenticate/join_league.html', {'form': form})


def leave_league(request, pk):
	user = request.user
	league = League.objects.get(pk=pk)
	UserLeagueParticipation.objects.filter(user=user, league=league).delete()
	return HttpResponseRedirect(reverse_lazy('players-urls:my_team'))



class LeagueList(ListView):

	model = League
	paginate_by = 20


	def get_queryset(self, **kwargs):
		user = self.request.user
		qs = super().get_queryset()
		return qs.filter(Q(owner=user) | Q(users__user=user))


class LeagueDetailView(DetailView):
	model = League

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		members = []
		for relation in self.object.users.all():
			user = relation.user
			team = Teams.objects.filter(owner=user).first()
			members.append((user, team))
		owner = self.object.owner
		owner_team = Teams.objects.filter(owner=owner).first()
		context['users'] = members + [(owner, owner_team), ]
		context['users'].sort(key=lambda x:x[1].get_team_total_points() if x[1] is not None else 0, reverse=True)
		return context


def league_delete(request, pk):
	league = League.objects.get(pk=pk)
	league.delete()
	return HttpResponseRedirect('main-urls:league_list')



#attempt at api content for news page
	#import requests
	#import json
	#api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=99509d87cbcb4b81ababc39ca20d8175")
	#api = json.loads(api_request.content)
	#return render(request, 'authenticate/news.html', {'api' : api })
