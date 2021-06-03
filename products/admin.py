from django.contrib import admin

from products.models import Product, ProductCategories

admin.site.register(ProductCategories)
admin.site.register(Product)