from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    context = {
        'title': "geeekshop"}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title' : "каталог",
        'header': 'добро пожаловать на сайт',
        'user'  : 'наш гость',
        'range' : [1,2,3] }

    context['products'] = Product.objects.all()
    categories = ProductCategory.objects.all()
    context['categories'] = categories

    return render(request, 'mainapp/products.html', context)

