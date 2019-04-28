from django.db import models
from players.models import Player

class Tournament(models.Model):
	date = models.TimeField()
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title


class PlayerTournamentRecord(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	tournament = models.ManyToManyField(Tournament, on_delete=models.CASCADE)
	score = models.IntegerField()

	def __str__(self):
		return self.player.name + " in " + self.tournament.title

	class Meta:
		verbose_name_plural = 'Players Tournament Records'
