from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class wallet(models.Model):

    # linking to the main user table
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # currencies
    toman = models.DecimalField(max_digits=32 , decimal_places=0 ,default=0)
    dollar = models.DecimalField(max_digits=16 , decimal_places=2 ,default=0)
    pound = models.DecimalField(max_digits=16 , decimal_places=2 ,default=0)


class price(models.Model):

    # currencies prices
    toman = models.DecimalField(max_digits=8, decimal_places=2, default=1)
    dollor = models.DecimalField(max_digits=8, decimal_places=2, default=115)
    pounds = models.DecimalField(max_digits=8, decimal_places=2, default=155)