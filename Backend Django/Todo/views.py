from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    return Response ({
    'LIST' : '/todo-list/',
    'DETAIL' : '/todo-detail/<str:pk>/',
    'CREATE' : '/todo-create',
    'UPDATE' : '/todo-update/<str:pk>/',
    'DELETE' : '/todo-delete/<str:pk>/'
    })

@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def todoUpdate(request, pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todos, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    todos = Todo.objects.get(id=pk)
    todos.delete()
    return Response("The Task has been deleted.")
