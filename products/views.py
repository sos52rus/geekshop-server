from django.shortcuts import render
import json
from geekshop.settings import BASE_DIR


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    with open(BASE_DIR / 'products/fixture/data.json', encoding='utf-8') as json_file:
        context = json.load(json_file)
    return render(request, 'products/products.html', context)
