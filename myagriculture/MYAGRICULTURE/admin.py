from django.contrib import admin
from .models import Customers, Box, Cart


admin.site.register(Customers)
admin.site.register(Box)
admin.site.register(Cart)