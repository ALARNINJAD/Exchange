from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # getting username and password
    
        if User.objects.filter(username=username).exists():
            return redirect('/login/')
        # if its already registered

        user = User.objects.create_user(username=username ,password=password)
        # create username
        
        return redirect('/login/')
        # now its time to log in

    return render(request,'register.html')


def log_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # getting username and password

        if not User.objects.filter(username=username).exists():
            return redirect('/register/')
        # if there is not that username

        user = authenticate(username=username,password=password)
        # authenticaion

        if user:
            login(request,user)
            return redirect('/home/')
        else:
            return redirect('/login/')
        # login

    return render(request,'login.html')