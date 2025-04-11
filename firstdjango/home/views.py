from django.shortcuts import render

def home_view(request):
    context = {}
    return render(request, "home/home.html", context)
# Create your views here.
