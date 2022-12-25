from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User, Client, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('User_code','Fullname','Mobile')

 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('Client_name','Company_name') 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields ='__all__'