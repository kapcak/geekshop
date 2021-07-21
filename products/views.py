from django.core import paginator
from django.shortcuts import render
from products.models import Product, ProductCategory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'geekshop - продукты',
        'categories': ProductCategory.objects.all()
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context=context)
