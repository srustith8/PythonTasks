from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# def apioverview(request):
#     return JsonResponse('API BASE POINT',safe=False)


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        "List":"/task-list",
        'Detail View': '/task-detail/<str:pk>',
        'Create':'/task-create',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskUpdate(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def taskDelete(request,pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response('item succesfully deleted')
