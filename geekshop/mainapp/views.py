from django.shortcuts import render

import json
import os

from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)
# Create your views here.


def index(request):
    context = {
        'title':'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Geekshop - Каталог',
    }

    # context['products'] = json.load(open(file_path, encoding='utf-8'))
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()

    return render(request, 'mainapp/products.html', context)


# 'products': [
#     {'name': 'Худи черного цвета с монограммами adidas Originals',
#      'price': 6090,
#      'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
#      'image': 'vendor/img/products/Adidas-hoodie.png',
#      },
#
#     {'name': 'Синяя куртка The North Face',
#      'price': 23725,
#      'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
#      'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
#      },
#
#     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
#      'price': 3390,
#      'description': 'атериал с плюшевой текстурой. Удобный и мягкий.',
#      'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
#      },
#
#     {'name': 'Черный рюкзак Nike Heritage',
#      'price': 2340,
#      'description': 'Плотная ткань. Легкий материал.',
#      'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
#      },
#
#     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
#      'price': 13590,
#      'description': 'Гладкий кожаный верх. Натуральный материал.',
#      'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
#      },
#
#     {'name': 'емно-синие широкие строгие брюки ASOS DESIGN',
#      'price': 2890,
#      'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
#      'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
#      },
# ]
