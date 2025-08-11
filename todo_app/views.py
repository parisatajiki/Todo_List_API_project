from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from todo_app.models import Todo
from todo_app.serializer import TodoSerializer




class AddTodo(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.validated_data['user'] = request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'user':'first login'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoList(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            todos = Todo.objects.filter(user=request.user)
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data)
        return Response({'user': 'first login'}, status=status.HTTP_400_BAD_REQUEST)


class TodoDelete(APIView):
    def delete(self, request, pk):
        if request.user.is_authenticated:
            Todo.objects.get(pk=pk).delete()
            return Response({'response':'deleted successfully'}, status=status.HTTP_200_OK)
        return Response({'user': 'first login'}, status=status.HTTP_400_BAD_REQUEST)


class TodoUpdate(APIView):
    def put(self, request, pk):
        if request.user.is_authenticated:
            todo = Todo.objects.get(pk=pk)
            if todo.user != request.user:
                return Response({'message': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
            serializer = TodoSerializer(data=request.data,instance=todo, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'user': 'first login'}, status=status.HTTP_400_BAD_REQUEST)




def str_to_bool(value):
    return value.lower() in ['true', '1', 'yes']
class TodoFiltterStatus(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'user': 'first login'}, status=status.HTTP_400_BAD_REQUEST)
        todos = Todo.objects.filter(user=request.user)
        statuss = request.data.get('status')
        if statuss is not None:
            status_bool = str_to_bool(statuss)
            todos = todos.filter(status=status_bool)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

