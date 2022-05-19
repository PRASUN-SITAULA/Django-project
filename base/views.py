from django import http
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'base/home.html',context)

def detail(request,pk):
    details = Post.objects.get(id=pk)
    context = {'details':details}
    return render(request,'base/details.html',context)

def new_post(request):
   form = PostForm()
   if request.method == "POST":
       form = PostForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect(home) 
       else:
           print(form.errors)
   return render(request, 'base/new_post.html', {'form':form})

def updatepost(request,pk):
    posts = Post.objects.get(id=pk)
    form = PostForm(instance=posts)
    if request.method == "POST":
       form = PostForm(request.POST, instance=posts)
       if form.is_valid():
            form.save()
            return redirect('detail', posts.pk)
    return render(request, 'base/update_post.html', {'form': form, 'posts': posts})
   
def deletepost(request,pk):
  posts = Post.objects.get(id=pk)
  if request.method == "POST":
    posts.delete()
    return redirect(home)
  return render(request, 'base/delete_post.html', {'posts':posts})

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, "Wrong username or password")
   
    return render(request, 'base/user_login.html', {})

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request, 'base/user_login.html', {})

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, "An error occured!!")
    return render(request, 'base/signup.html', {'form': form})



        

    