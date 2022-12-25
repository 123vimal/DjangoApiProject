from django.db import models

# Create your models here.

class User(models.Model):
    User_code=models.CharField(max_length=3)
    Fullname=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    

class Client(models.Model):
    Client_name=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)

class Project(models.Model):
    Project_Name=models.CharField(max_length=100)
    Created_by=models.CharField(max_length=100)

    