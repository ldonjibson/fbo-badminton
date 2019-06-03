from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import csv
from pycountry_convert import country_name_to_country_alpha2
from players.models import *

from django.contrib.admin.views.decorators import staff_member_required

PLAYER_ATTRIBUTES = [
    'rank',
    'country',
    'cost',
    'score',
    'status',
    'current_tournament_score',
    'last_tournament_score',
]

@staff_member_required
def upload_csv(request):
    data = {'fields': PLAYER_ATTRIBUTES}
    if request.method == "POST":
        try:
            csv_file = request.FILES["csv_file"]
            # check for file format
            if not csv_file.name.endswith('.csv'):
                messages.error(request,'File is not CSV type')
                return HttpResponseRedirect(reverse("upload-csv"))

            # do necessary operations to read the request file
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)


            for row in reader:
                type = row.get('type')[:2]
                name = row.get('name')
                if not type or not name:
                    continue # skip if no type or name in the CSV row

                # below we get a player with the row type and the given name or we create one
                player, _ = eval(type.upper() + 'Player.objects.get_or_create(name="{name}")'.format(name=name))

                # below we get team name if one is given and assign the player to that team.
                # we don't create a new team if it doesn't exist(discussable)
                team_name = row.get('team')
                if team_name:
                    team = Team.objects.filter(name=team_name).first()
                    if team:
                        player.team_id = team.id

                # parse remaining attributes, any that exist on the player model and are present in PLAYER_ATTRIBUTES,
                # will drop an error if the datatypes don't match(digit for a name, string for a number) etc.
                for attribute in PLAYER_ATTRIBUTES:
                    csv_attribute_value = row.get(attribute)
                    if csv_attribute_value: # skip if no attribute in CSV row
                        setattr(player, attribute, csv_attribute_value) # set attribute for player
                if len(player.country) != 2:
                    try:
                        player.country = country_name_to_country_alpha2(player.country, cn_name_format="default")
                    except KeyError:
                        print("Invalid Country Name, setting to default. You may change the country in CSV and upload "
                              "the file again. It'll update the country name.")
                player.save()
                print(player)


        except Exception as e:
            print(e)
            messages.error(request,"Unable to upload file. "+repr(e))

    return render(request, "mysite/upload_csv.html", data)