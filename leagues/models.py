from django.db import models

# Create your models here.
from mysite import settings


class League(models.Model):
	name = models.CharField(max_length=50)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='owned_leagues')
	invite_key = models.CharField(max_length=32)
	members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='UserLeagueParticipation')

	def __str__(self):
		return self.name

class UserLeagueParticipation(models.Model):
	league = models.ForeignKey(League, related_name='users', on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='leagues', on_delete=models.CASCADE)
	date_joined = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.league.name + ' --- ' + self.user.username