from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.urls import reverse
from mainapp.models import Product,ProductCategory
from admins.forms import ProductAdminRegisterForm,CategoryAdminRegisterForm

from admins.forms import CategoryAdminProfileForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context ={
        'users': User.objects.all()
    }
    return render(request, 'admins/admins-users-read.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form' : form
    }
    return render(request, 'admins/admins-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request,pk):
    user_select = User.objects.get(pk=pk)
    if request.method == 'POST':
            form = CategoryAdminProfileForm(data=request.POST,instance=user_select, files=request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Редактирование',
        'form': form,
        'user_select': user_select,
    }
    return render(request, 'admins/admins-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))




@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context ={
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products-read.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminRegisterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Создание товара',
        'form' : form
    }
    return render(request, 'admins/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request,pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductAdminRegisterForm(data=request.POST, instance=product_select,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:

        form = ProductAdminRegisterForm(instance=product_select)
    context = {
        'title': 'Geekshop - Админ | Редактирование товара',
        'form': form,
        'product_select': product_select,
    }

    return render(request, 'admins/admin-products-update-delete.html',context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request,pk):
    select_product = Product.objects.get(pk=pk)
    select_product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))



@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context ={
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-categories-read.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):

    if request.method == 'POST':
        data = {'name': request.POST.get("name"),
                'description': request.POST.get("description")
                }
        form = CategoryAdminRegisterForm(data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
        else:
            print(form.errors)
    else:
        form = CategoryAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Создание категории',
        'form' : form
    }
    return render(request, 'admins/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request,pk):
    category_select = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryAdminProfileForm(data=request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:

        form = CategoryAdminRegisterForm(instance=category_select)
    context = {
        'title': 'Geekshop - Админ | Редактирование',
        'form': form,
        'category_select': category_select,
    }
    return render(request, 'admins/admin-categories-update-delete.html',context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request,pk):
    select_category = ProductCategory.objects.get(pk=pk)
    select_category.delete()
    return HttpResponseRedirect(reverse('admins:admin_categories'))






