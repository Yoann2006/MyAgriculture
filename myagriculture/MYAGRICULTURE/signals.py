from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customers, Cart

@receiver(post_save, sender=Customers)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(customer=instance)
