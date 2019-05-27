from django.db import models
from django_countries.fields import CountryField
from authenticate.models import Teams


class Player(models.Model):

	STATUS_CHOICES = [('active', 'Playing'),
			   ('notactive', 'Not Playing')
			   ]

	rank = models.IntegerField(default=10)
	name = models.CharField(max_length=50, default="Default name")
	country = CountryField(blank_label='(select country)', default='US')
	cost = models.FloatField(default=10) # price is a number, defaults to 10. You can set it up in the admin panel
	score = models.IntegerField(default=0)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='1')
	picture = models.ImageField(default='default.png', blank=True)
	current_tournament_score = models.IntegerField(default=10)
	last_tournament_score = models.IntegerField(default=10)

	def __str__(self):
		return self.name

	def get_type(self): # MS, WS, etc
		return self.__class__.__name__[:2]

	def get_profile_stats(self):
		STATS = ['score', 'status', 'current_tournament_score', 'last_tournament_score', 'rank']
		stats = [(stat.replace('_', ' ').title(), getattr(self, stat)) for stat in STATS]
		return stats

class MSPlayer(Player):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='MSplayers', null=True, blank=True)  # connection to a team


class WSPlayer(Player):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='WSplayers', null=True, blank=True)  # connection to a team


class MDPlayer(Player):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='MDplayers', null=True, blank=True)  # connection to a team


class WDPlayer(Player):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='WDplayers', null=True, blank=True)  # connection to a team


class XDPlayer(Player):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='XDplayers', null=True, blank=True)  # connection to a team