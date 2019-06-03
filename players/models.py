from django.db import models
from django_countries.fields import CountryField

from teams.models import Team


class Player(models.Model):

	STATUS_CHOICES = [('active', 'Playing'),
			   ('notactive', 'Not Playing')
			   ]

	rank = models.IntegerField(default=10)
	name = models.CharField(max_length=50)
	country = CountryField(blank_label='(select a country)', default='CN')
	cost = models.FloatField(default=3) # price is a number, defaults to 3. You can set it up in the admin panel
	score = models.IntegerField(default=0)
	form = models.IntegerField(default=0)
	career_winrate = models.IntegerField(default=0)
	year_winrate = models.IntegerField(default=0)
	current_tournament_score = models.IntegerField(default=0)
	last_tournament_score = models.IntegerField(default=0)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='1')
	picture = models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return self.name

	def get_type(self): # MS, WS, etc
		return self.__class__.__name__[:2]

	def get_profile_stats(self):
		STATS = ['score', 'status', 'current_tournament_score', 'last_tournament_score', 'rank']
		stats = [(stat.replace('_', ' ').title(), getattr(self, stat)) for stat in STATS]
		return stats

class MSPlayer(Player):
	team = models.ManyToManyField(Team, related_name='MSplayers', blank=True)  # connection to a team


class WSPlayer(Player):
	team = models.ManyToManyField(Team, related_name='WSplayers', blank=True)  # connection to a team


class MDPlayer(Player):
	team = models.ManyToManyField(Team, related_name='MDplayers', blank=True)  # connection to a team


class WDPlayer(Player):
	team = models.ManyToManyField(Team, related_name='WDplayers', blank=True)  # connection to a team


class XDPlayer(Player):
	team = models.ManyToManyField(Team, related_name='XDplayers', blank=True)  # connection to a team
