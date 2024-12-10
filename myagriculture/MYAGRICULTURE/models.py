from django.db import models

# Create your models here.
class Customers(models.Model):          
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=8)