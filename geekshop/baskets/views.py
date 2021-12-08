from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from mainapp.models import Product
from baskets.models import Basket


@login_required
def basket_add(request,id):
    user_select = request.user
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=user_select, product=product)
    ff = open('test_output.txt','a',encoding='utf-8')
    ff.write('hello, add basket!\n')
    if baskets:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        ff.write(f'add in old basket {basket.quantity}\n')
    else:
        Basket.objects.create(user=user_select, product=product,quantity=1)
        ff.write(f'add in NEW basket 1\n')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request,id):
    Basket.objects.get(id=id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
