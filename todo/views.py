from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from todo.models import Todo
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    class IsOwner(IsAuthenticated):
        def has_object_permission(self, request, view, obj):
            return obj.owner == request.user
        
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwner]
