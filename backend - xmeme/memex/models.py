from django.db import models
from django.core import validators as v

# Create your models here.
class memeinfo(models.Model):
    name = models.CharField(max_length=100)
    caption  = models.TextField(null=True)
    url = models.URLField(max_length=250)

