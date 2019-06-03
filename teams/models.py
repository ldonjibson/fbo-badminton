from django.db import models

# Create your models here.
from django.db.models import Sum

from mysite import settings


class Team(models.Model):  # team model, players(Rankings model) have foreign key relation to it
    budget = models.IntegerField(default=120)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='teams')  # relation to a user
    name = models.SlugField()
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


class ArchiveRecord(models.Model):  # an archive record
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # relation to a team
    score = models.IntegerField()  # score


