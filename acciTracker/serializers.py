from rest_framework import serializers
from .models import *


class AccidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accident
        fields = ['datetime', 'lat', 'lng']

class AccidentSendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accident
        fields = ['id', 'datetime', 'lat', 'lng']
