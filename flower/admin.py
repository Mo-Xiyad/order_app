from django.contrib import admin
from .models import Order, BouquetType, Product


admin.site.register(Order),
admin.site.register(BouquetType),
admin.site.register(Product),