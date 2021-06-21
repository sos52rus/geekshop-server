from django.shortcuts import render

from products.models import Product, ProductCategories


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context = {
        "title": "geekShop - Каталог",
        "products": product,
        "product_categories": ProductCategories.objects.all(),
    }
    return render(request, 'products/products.html', context)
