from django.db import models
from django.conf import settings
from django.db.models import Sum


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

	def get_team_value(self):
		total = []
		total.append(self.MSplayers.all().aggregate(Sum('cost'))['cost__sum'])
		total.append(self.WSplayers.all().aggregate(Sum('cost'))['cost__sum'])
		total.append(self.MDplayers.all().aggregate(Sum('cost'))['cost__sum'])
		total.append(self.WDplayers.all().aggregate(Sum('cost'))['cost__sum'])
		total.append(self.XDplayers.all().aggregate(Sum('cost'))['cost__sum'])
		total = [x for x in total if x is not None]
		return sum(total)



class ArchiveRecord(models.Model): # an archive record
	team = models.ForeignKey(Teams, on_delete=models.CASCADE) # relation to a team
	score = models.IntegerField() # score


class Ranking(models.Model):
	rank = models.IntegerField(default=10)
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	cost = models.FloatField(default=10) # price is a number, defaults to 10. You can set it up in the admin panel
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
	current_tournament_score = models.IntegerField(default=10)
	last_tournament_score = models.IntegerField(default=10)

	def __str__(self):
		return str(self.rank) + ' ' + self.name + ' ' + str(self.playing)

	def get_type(self): # MS, WS, etc
		return self.__class__.__name__[:2]

#small subclasses for each type of player, they have all the methods from Ranking model, but also related to a team)

class MSPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='MSplayers', null=True)  # connection to a team


class WSPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='WSplayers', null=True)  # connection to a team


class MDPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='MDplayers', null=True)  # connection to a team


class WDPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='WDplayers', null=True)  # connection to a team


class XDPlayer(Ranking):
	team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='XDplayers', null=True)  # connection to a team


