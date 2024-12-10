from django.db import models

# Create your models here.
    
class Box(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField(default=0)
    product_kilo = models.IntegerField(default=0)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.OneToOneField('Customers', on_delete=models.CASCADE, related_name="cart")
    products = models.ManyToManyField(Box, related_name="carts")

class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=8)
