from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import loginform

# Create your views here.

def login_view(request):
    form = loginform()
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home/")
        else:
            messages.info(request, "username or password is not correct")
            form = loginform()
    
    context = {"form": form}
    return render(request, "login/login.html", context)
