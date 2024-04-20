from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import todo
from .serializers import ToDoSerializer
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.response import Response

@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        todo_list = todo.objects.all()
        serializer = ToDoSerializer(todo_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def individual(request, id):
    try:
        ins = todo.objects.get(pk=id)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = ToDoSerializer(ins)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ToDoSerializer(ins, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

