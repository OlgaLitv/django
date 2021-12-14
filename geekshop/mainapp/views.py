from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    context = {
        'title': "geeekshop"}
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=0,page=1):
    context = {
        'title' : "каталог",
        'header': 'добро пожаловать на сайт',
        'user'  : request.user,
        'range' : [1,2,3],
        'category': id_category
    }

    if id_category: # если 0, то идем в else и выводим все продукты
        products = Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()


    p = Paginator(products, 3)
    categories = ProductCategory.objects.all()
    context['categories'] = categories

    try:
        products_paginator = p.page(page)
    except PageNotAnInteger:
        products_paginator = p.page(1)
    except EmptyPage:
        products_paginator = p.page(p.num_pages)

    context['products'] = products_paginator

    return render(request, 'mainapp/products.html', context)


def details(request, product_id):
    context = {
        'title' : "Geekshop",
        'user'  : request.user
    }

    context['product'] = Product.objects.get(id=product_id)

    return render(request, 'mainapp/details.html', context)
