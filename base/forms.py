from django import forms
from curses import use_default_colors
from django.forms import ModelForm
from .models import Post
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
       
# class CustomUserCreationField(UserCreationForm):
#     class meta:
#         model = CustomUser
#         fields = '__all__'