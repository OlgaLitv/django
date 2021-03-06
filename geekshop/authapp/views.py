from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth, messages
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.urls import reverse
from authapp.models import User
from baskets.models import Basket


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            repeat_email_count = User.objects.filter(email=email).count()
            #если нашли пользователя с таким же email, то не создаем нового, это ошибка
            if repeat_email_count == 0:
                form.save()
                messages.success(request, 'Вы успешно зарегистрированы')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                print(form.errors)
        else:
            print(form.errors)

    else:
        form = UserRegisterForm()

    context = {
        'title': "Geekshop | Регистрация пользователя",
        'form': form
        }
    return render(request, 'authapp/register.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    else:
        form = UserLoginForm()

    context = {
        'title': "Geekshop | Авторизация",
        'form': form
    }
    return render(request, 'authapp/login.html', context)


@login_required
def profile(request):
    form = UserProfileForm(instance=request.user)
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно сохранены!')
        else:
            print(form.errors)

    context = {
        'title': 'Geekshop | Профайл',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
