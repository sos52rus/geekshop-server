from django.shortcuts import render

from products.models import Product, ProductCategories


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        "title": "geekShop - Каталог",
        "products": Product.objects.all().values(),
        "product_categories": ProductCategories.objects.all().values(),
    }
    return render(request, 'products/products.html', context)
