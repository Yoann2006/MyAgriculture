from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from .add_user import add_user
from .display_box import display_box
from .add_to_box import add_to_cart

urlpatterns = [
    path('', lambda request : redirect('admin/')),
    path('add_user/', add_user, name='add_user'),
    path('add_to_box/<int:customer_id>/', add_to_cart, name='add_to_box'),
    path('display_box/<int:customer_id>/', display_box, name='display_box'),
]
