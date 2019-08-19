from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import auth
from .forms import LoginForm
from .models import blogModel
from datetime import datetime


# Create your views here.
def home(request):
    blogs=blogModel.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            #give permission to login
            auth.login(request,user)
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials!!")
            return redirect("login")

    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return render(request,'home.html',{})

def create(request):
    return render(request,'create.html',{})
    
def register(request):
    return render(request,'register.html',{})


