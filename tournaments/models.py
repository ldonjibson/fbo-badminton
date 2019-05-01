from django.db import models
from django_countries.fields import CountryField

from authenticate.models import League
from players.models import Player

class Tournament(models.Model):
	date = models.TimeField()
	title = models.CharField(max_length=255)
	country = CountryField(blank_label='(select country)', default='GB')
	league = models.ManyToManyField(League)

	def __str__(self):
		return self.title


class PlayerTournamentRecord(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='tournament_records')
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	score = models.IntegerField()
	game8 = models.IntegerField()
	match8 = models.IntegerField()
	bonus = models.IntegerField()

	def __str__(self):
		return self.player.name + " in " + self.tournament.title

	class Meta:
		verbose_name_plural = 'Players Tournament Records'
