from django.db import models
from players.models import Player

class Tournament(models.Model):
	date = models.TimeField()
	title = models.CharField(max_length=255)


class PlayerTournamentRecord(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	score = models.IntegerField()

	class Meta:
		verbose_name_plural = 'Players Tournament Records'
