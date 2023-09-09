from django.shortcuts import render
from .models import Task
from .serializers import taskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        taskdata=Task.objects.all()
        serial=taskSerializer(taskdata,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getid(request,id):
    try:
        taskid=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=taskSerializer(taskid)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        taskid=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=taskSerializer(taskid)
        return Response(serial.data,status=status.HTTP_200_OK)

    if request.method=='DELETE':
        Task.delete(taskid)     # code to delete selected id
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=taskSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        taskid=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=taskSerializer(taskid)
        return Response(serial.data,status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        serial=taskSerializer(data=request.data,instance=taskid) 
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
    
