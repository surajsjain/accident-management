from datetime import datetime

from django.shortcuts import render, redirect

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *
# Create your views here.

## Post accidents from Raspberry Pi
@api_view(['GET', 'POST'])
def alertacci(request):

    if request.method == 'POST':
        serializer = AccidentSerializer(data=request.data)
        # print(request.data)
        # datetime_str = request.data['datetime']
        #
        #
        # datetime_object = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S')
        #
        # print(type(datetime_object))
        # print(datetime_object)  # printed in default format

        if serializer.is_valid():
            # print(serializer.data)
            print('Data is valid')
            serializer.save()

            registerdAccident = Accident.objects.filter(lat=request.data['lat']).filter(lng=request.data['lng']).filter(datetime=request.data['datetime'])[0]
            c = Crowd()
            c.datetime = registerdAccident.datetime
            c.accident = registerdAccident
            c.count = 0
            c.save()

            responseData = {
                'id': registerdAccident.id,
            }

            return Response(responseData, status=status.HTTP_201_CREATED)
            # return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## Get accidents into the web app via AJAX
@api_view(['GET', 'POST'])
def getActiveAcci(request):
    if request.method == 'GET':
        accidents = Accident.objects.filter(handled=False)
        serializer = AccidentSendSerializer(accidents, many=True)
        return Response(serializer.data)

def deactivateAcci(request, acci_id):
    accident = Accident.objects.filter(id=acci_id)
    accident.handled = True
    accident.save()
