from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class List(models.Model):
    name = models.CharField(max_length=100, unique=True)
    board_name = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    end_date = models.DateField() 