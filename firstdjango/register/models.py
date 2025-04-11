from django.db import models

# Create your models here.
class Order(models.Model):
    email = models.EmailField(max_length = 254)
    user = models.CharField(max_length = 150)
    passw = models.CharField(max_length = 128)