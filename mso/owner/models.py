from django.db import models
from django.contrib.auth.models import User

 
class Products(models.Model):
    barcode = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(default="(No Description Available)")
    super = models.IntegerField()
    super = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)


class Cashiers(models.Model):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(default="(No Email)")
    password = models.CharField(max_length=100)
    super = models.IntegerField()
    super = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    
