from django.shortcuts import get_object_or_404
from .models import Cart, Box
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def display_box(request, customer_id):
    cart = get_object_or_404(Cart, customer_id=customer_id)
    products = cart.products.all()

    box_details = [
        {
            "product_name": product.product_name,
            "product_price": product.product_price,
            "product_kilo": product.product_kilo
        }
        for product in products
    ]

    return JsonResponse({
        "success": True,
        "cart_id": cart.id,
        "products": box_details
    })
