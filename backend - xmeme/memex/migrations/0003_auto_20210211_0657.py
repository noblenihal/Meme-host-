# Generated by Django 3.1.5 on 2021-02-11 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memex', '0002_auto_20210211_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memeinfo',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
