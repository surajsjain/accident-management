from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Accident)
admin.site.register(Crowd)
admin.site.register(AccidentReport)
admin.site.register(VehicleReport)
