from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'geekshop - продукты',
    }
    return render(request, 'products/products.html', context=context)
