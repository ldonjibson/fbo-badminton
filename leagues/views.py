from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from leagues.forms import KeyForm
from leagues.models import *
from teams.models import Team


def league_delete(request, pk):
	league = League.objects.get(pk=pk)
	league.delete()
	return HttpResponseRedirect('main-urls:league_list')


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

	return render(request, 'authenticate/../templates/leagues/league_join.html', {'form': form})


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
			team = Team.objects.filter(owner=user).first()
			members.append((user, team))
		owner = self.object.owner
		owner_team = Team.objects.filter(owner=owner).first()
		context['users'] = members + [(owner, owner_team), ]
		context['users'].sort(key=lambda x:x[1].get_team_total_points() if x[1] is not None else 0, reverse=True)
		return context
