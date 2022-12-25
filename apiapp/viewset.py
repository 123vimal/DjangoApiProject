from rest_framework import viewsets
from .import models
from .import serializer

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
     queryset = models.User.objects.all()
     serializer_class = serializer.UserSerializer

class ClientViewset(viewsets.ModelViewSet):
     queryset = models.Client.objects.all()
     serializer_class = serializer.ClientSerializer

class ProjectViewset(viewsets.ModelViewSet):
     queryset = models.Project.objects.all()
     serializer_class = serializer.ProjectSerializer
 