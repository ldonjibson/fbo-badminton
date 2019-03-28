from django.db import models
from django.conf import settings


class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + '...'	 


class Teams(models.Model): # team model, players(Rankings model) have foreign key relation to it
	budget = models.IntegerField(default=120)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) # relation to a user
	team = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)
	points = models.CharField(max_length=50)
	

	def __str__(self):
		return self.owner.username


class Ranking(models.Model):
	rank = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	price = models.IntegerField(default=10) # price is a number, defaults to 10. You can set it up in the admin panel
	event = models.CharField(max_length=50)
	score = models.CharField(max_length=50)
	last = models.CharField(max_length=50)
	form = models.CharField(max_length=50)
	results = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	game8 = models.CharField(max_length=50)
	match8 = models.CharField(max_length=50)
	player = models.SlugField()
	picture = models.ImageField(default='default.png', blank=True)
	playing = models.BooleanField(default=True)


	def __str__(self):
		return self.rank + ' ' + self.name + ' ' + str(self.playing)

#small subclasses for each type of player, they have all the methods from Ranking model, but also related to a team)

class MSPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='MSplayers')  # connection to a team


class WSPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='WSplayers')  # connection to a team


class MDPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='MDplayers')  # connection to a team


class WDPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='WDplayers')  # connection to a team


class XDPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='XDplayers')  # connection to a team


class ArchiveRecord(models.Model): # an archive record
	team = models.ForeignKey(Teams, on_delete=models.CASCADE) # relation to a team
	score = models.IntegerField() # score