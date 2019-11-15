from django.db import models
from datetime import datetime

# Create your models here.
class Accident(models.Model):
    datetime = models.DateTimeField(default=datetime.now())
    lat = models.FloatField();
    lng = models.FloatField();

class Crowd(models.Model):
    datetime = models.DateTimeField(default=datetime.now())
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, blank=True)

class AccidentReport(models.Model):
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE)

    n_people_involved = models.IntegerField(default=0)
    n_children_involved = models.IntegerField(default=0)

    n_injured = models.IntegerField(default=0)
    n_dead = models.IntegerField(default=0)

    mistake = models.CharField(max_length = 50, default='Not Determined')

    comment = models.CharField(max_length = 700, blank=True)

class VehicleReport(models.Model):
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE)

    vehicle_type = models.CharField(max_length=40)
    n_wheels = models.IntegerField(default=2)
    vehicle_number = models.CharField(max_length=50)
    vehicle_maker = models.CharField(max_length=70)
    vehicle_model = models.CharField(max_length=70)

    n_passengers_dead = models.IntegerField()
    n_passengers_injured = models.IntegerField()
