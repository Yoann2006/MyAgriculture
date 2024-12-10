from django.http import JsonResponse
from .models import Customers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            phone_number = data.get("phone_number")
            password = data.get("password")

            if not phone_number or not password:
                return JsonResponse({
                    "success": False,
                    "message": "Le numéro de téléphone et le mot de passe sont obligatoires."
                }, status=400)

            if Customers.objects.filter(phone_number=phone_number).exists():
                return JsonResponse({
                    "success": False,
                    "message": "Un utilisateur avec ce numéro de téléphone existe déjà."
                }, status=400)

            new_user = Customers.objects.create(
                phone_number=phone_number,
                password=password
            )

            return JsonResponse({
                "success": True,
                "message": "Utilisateur créé avec succès.",
                "user": {
                    "id": new_user.id,
                    "phone_number": new_user.phone_number
                }
            }, status=200)
        except json.JSONDecodeError:
            return JsonResponse({
                "success": False,
                "message": "Données JSON invalides."
            })
    return JsonResponse({"success": False, "message": "Seules les requêtes POST sont autorisées."}, status=400)
