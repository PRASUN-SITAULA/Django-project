from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    def __str__(self):
        return self.title

#  class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(auto_now=False, blank=False)
    
   