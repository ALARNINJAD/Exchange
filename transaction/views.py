from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import price,wallet
from decimal import Decimal

# Create your views here.
@login_required(login_url='/login/')

def home(request):
    
    # create or get the user wallet
    user_wallet, created = wallet.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        
        # adding balance to the wallet
        add_toman = request.POST.get('add_toman')
        if add_toman:
            user_wallet.toman += Decimal(add_toman)
            user_wallet.save()

        


    return render(request,'home.html',{"user_wallet":user_wallet})