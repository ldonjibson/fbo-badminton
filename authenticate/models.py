from django.db import models

class Ranking(models.Model):
	rank = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	price = models.CharField(max_length=50)
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


class Teams(models.Model):
	username = models.CharField(max_length=100)
	team = models.SlugField()
	MS1 = models.CharField(max_length=50)
	MS2 = models.CharField(max_length=50)
	WS1 = models.CharField(max_length=50)
	WS2 = models.CharField(max_length=50)
	MD1 = models.CharField(max_length=50)
	MD2 = models.CharField(max_length=50)
	WD1 = models.CharField(max_length=50)
	WD2 = models.CharField(max_length=50)
	XD1 = models.CharField(max_length=50)
	XD2 = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True)
	points = models.CharField(max_length=50)
	

	def __str__(self):
		return self.username		