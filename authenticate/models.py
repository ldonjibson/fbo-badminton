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
	owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='teams') # relation to a user
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


	def get_team_total_points(self):
		total = []
		total.append(self.MSplayers.all().aggregate(Sum('score'))['score__sum'])
		total.append(self.WSplayers.all().aggregate(Sum('score'))['score__sum'])
		total.append(self.MDplayers.all().aggregate(Sum('score'))['score__sum'])
		total.append(self.WDplayers.all().aggregate(Sum('score'))['score__sum'])
		total.append(self.XDplayers.all().aggregate(Sum('score'))['score__sum'])
		total = [x for x in total if x is not None]
		return sum(total)



class ArchiveRecord(models.Model): # an archive record
	team = models.ForeignKey(Teams, on_delete=models.CASCADE) # relation to a team
	score = models.IntegerField() # score



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

# class Tournament(models.Model):
