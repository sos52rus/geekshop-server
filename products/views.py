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
        "products": Product.objects.all(),
        "product_categories": ProductCategories.objects.all(),
    }
    return render(request, 'products/products.html', context)
