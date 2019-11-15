from django.shortcuts import render, redirect

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
# Create your views here.

## Post accidents from Raspberry Pi
@api_view(['GET', 'POST'])
def alertacci(request):

    if request.method == 'POST':
        serializer = AccidentSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
