# Generated by Django 2.1.5 on 2019-02-05 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranking',
            old_name='nationality',
            new_name='country',
        ),
    ]
