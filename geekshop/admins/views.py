from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.urls import reverse, reverse_lazy
from mainapp.models import Product,ProductCategory
from admins.forms import ProductAdminForm,CategoryAdminForm
from django.views.generic import ListView, CreateView,UpdateView,DeleteView,DetailView,TemplateView
from mainapp.mixin import BaseClassContextMixin, UserDispatchMixin


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


class UserListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admins-users-read.html'
    title = 'Админка | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admins-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Админка | Пользователи'
    success_url = reverse_lazy('admins:admin_users')



class UserUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admins-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Редактирование пользователя'
    success_url = reverse_lazy('admins:admin_users')


class UserDeleteView(DeleteView, UserDispatchMixin):
    model = User
    template_name = 'admins/admins-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(success_url)




class ProductListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    title = 'Админка | Товары'


class ProductCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductAdminForm
    title = 'Админка | Новый товар'
    success_url = reverse_lazy('admins:admin_products')


class ProductUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAdminForm
    title = 'Админка | Редактирование товара'
    success_url = reverse_lazy('admins:admin_products')


class ProductDeleteView(DeleteView, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAdminForm
    success_url = reverse_lazy('admins:admin_products')




class CategoryListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    title = 'Админка | Категории'


class CategoryCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoryAdminForm
    title = 'Админка | Новая категория'
    success_url = reverse_lazy('admins:admin_categories')


class CategoryUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryAdminForm
    title = 'Админка | Редактирование категории'
    success_url = reverse_lazy('admins:admin_categories')



class CategoryDeleteView(DeleteView, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryAdminForm
    success_url = reverse_lazy('admins:admin_categories')




