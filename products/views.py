from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'path_img': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face',
             'price': 23725,
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'path_img': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': 3390,
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'path_img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage',
             'price': 2340,
             'description': 'Плотная ткань. Легкий материал.',
             'path_img': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590,
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'path_img': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': 2890,
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'path_img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        ],
    }
    return render(request, 'products/products.html', context)