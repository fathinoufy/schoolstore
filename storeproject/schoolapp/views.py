from django.contrib import messages
from django.contrib.auth.context_processors import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            error_message
    else:
        ''

    return render(request,"login.html")
def form(request):
    if request.method=='POST':
        messages.success(request,'Order Confirmed')
        return redirect('form')
    else:
        return render(request,'form.html')

def register(request):
    return render(request, "register.html")

def new_page(request):
    return render(request,"newpage.html")

def logout(request):
    auth.logout(request)
    return redirect('/')