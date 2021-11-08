from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



def home(request):
    return HttpResponse("<center><h1 style='background-color:powderblue'>Welcome to apiTodo</h1></center>")




@api_view(['GET'])
def todoList(request):
    querset = Todo.objects.all()

    serializer = TodoSerializer(querset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todoListCreate(request):
    serializer = TodoSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def toDo_list(request):
    if request.method == 'GET':
        querset = Todo.objects.all()

        serializer = TodoSerializer(querset, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

