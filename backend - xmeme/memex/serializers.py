from django.db.models import fields
from rest_framework import serializers
from .models import memeinfo

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = memeinfo
        fields = '__all__'