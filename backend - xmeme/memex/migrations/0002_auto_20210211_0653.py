# Generated by Django 3.1.5 on 2021-02-11 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memeinfo',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
