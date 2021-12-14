from authapp.forms import UserRegisterForm
from django import forms
from authapp.models import User
from authapp.forms import UserProfileForm
from django.forms import ModelForm
from mainapp.models import Product, ProductCategory


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(),required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductAdminRegisterForm(ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super(ProductAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название продукта'
        self.fields['description'].widget.attrs['placeholder'] = 'Введите описание продукта'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Введите количество товара на складе'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите цену'
        self.fields['category'].widget.attrs['placeholder'] = 'Выберите категорию'

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
        self.fields['category'].widget.attrs['class'] = 'related-widget-wrapper'


class CategoryAdminRegisterForm(ModelForm):

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminRegisterForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class CategoryAdminProfileForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminProfileForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'




