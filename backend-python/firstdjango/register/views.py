from django.shortcuts import render
from .forms import orderform,createuserform
from django.contrib import messages
# Create your views here.

def register_view(request):
    form = createuserform()
    if request.method == "POST":
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'you are now')

    context = {"form": form}
    return render(request, "register/register.html",context)
