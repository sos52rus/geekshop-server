from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from products.models import Product, ProductCategories


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(product, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        "title": "geekShop - Каталог",
        "products": products_paginator,
        "product_categories": ProductCategories.objects.all(),
    }
    return render(request, 'products/products.html', context)
