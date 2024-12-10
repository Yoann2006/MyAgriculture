from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Cart, Box
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_to_cart(request, customer_id):
    if request.method == "POST":
        data = json.loads(request.body)
        cart = get_object_or_404(Cart, customer_id=customer_id)

        product_name = data.get('product_name')
        product_price = data.get('product_price')
        product_kilo = data.get('product_kilo')

        if not all([product_name, product_price, product_kilo]):
            return JsonResponse({
                "success": False,
                "message": "Veuillez fournir le nom, le prix et le nombre de kilos du produit."
            }, status=400)

        box, created = Box.objects.get_or_create(
            product_name=product_name,
            product_price=product_price,
            product_kilo=product_kilo
        )

        cart.products.add(box)

        return JsonResponse({
            "success": True,
            "message": f"Le produit '{product_name}' a été ajouté au panier du client.",
            "box": {
                "product_name": box.product_name,
                "product_price": box.product_price,
                "product_kilo": box.product_kilo
            }
        }, status=200)

    return JsonResponse({"success": False, "message": "Seules les requêtes POST sont autorisées."}, status=400)
