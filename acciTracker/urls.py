from django.urls import path, include
from .views import *

urlpatterns = [
    path('alertacci/', alertacci),
    path('getactiveacci/', getActiveAcci),
    path('deactivate/<int:acci_id>/', deactivateAcci, name='handled'),
]
