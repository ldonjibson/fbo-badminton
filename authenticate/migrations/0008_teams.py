# Generated by Django 2.1.5 on 2019-03-02 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_auto_20190224_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('team', models.SlugField()),
                ('MS1', models.TextField()),
                ('MS2', models.TextField()),
                ('WS1', models.TextField()),
                ('WS2', models.TextField()),
                ('MD1', models.TextField()),
                ('MD2', models.TextField()),
                ('WD1', models.TextField()),
                ('WD2', models.TextField()),
                ('XD1', models.TextField()),
                ('XD2', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
