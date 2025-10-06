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
        if 'add_toman' in request.POST:

            # adding balance to the wallet
            add_toman = request.POST.get('add_toman')
            if add_toman:
                user_wallet.toman += Decimal(add_toman)
                user_wallet.save()

        elif 'from_currency' or 'to_currency' in request.POST:

            # getting transactions inputs
            from_currency = request.POST.get('from-currency')
            to_currency = request.POST.get('to-currency')
            amount = Decimal(request.POST.get('amount'))

            # setting a map for different options
            current_price = price.objects.first()
            rates = {
                'toman': {
                    'dollar': Decimal(1) / current_price.dollar,
                    'pound': Decimal(1) / current_price.pound,
                    'toman': Decimal(1),
                },
                'dollar': {
                    'toman': current_price.dollar,
                    'pound': current_price.dollar / current_price.pound,
                    'dollar': Decimal(1),
                },
                'pound': {
                    'toman': current_price.pound,
                    'dollar': current_price.pound / current_price.dollar,
                    'pound': Decimal(1),
                }
            }

            # calculate
            if getattr(user_wallet,from_currency) >= amount >=0 :
                result = amount * rates[from_currency][to_currency]
                setattr(user_wallet, from_currency, getattr(user_wallet, from_currency) - amount)
                setattr(user_wallet, to_currency, getattr(user_wallet, to_currency) + result)
                user_wallet.save()

    return render(request,'home.html',{"user_wallet":user_wallet})