from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

menu = [
    {'title': 'Товары', 'url_name': 'product'},
    {'title': 'Корзина', 'url_name': 'card'},
]


def home_page(request):
    data = {
        'title': 'Главная страница',
        'menu': menu
    }
    return render(request, 'platform.html', context=data)


def shop_page(request):
    games = Game.objects.all()
    data_db = {
        'title': 'Магазин',
        'menu': menu,
        'products': games,
    }

    return render(request, 'product.html', context=data_db)


def cart_page(request):
    context = {
        'title': 'Корзина',
        'content': "Извините, Ваша корзина пуста",
        'menu': menu,
    }

    return render(request, 'cart.html', context=context)


# Псевдо-список существующих пользователей

users = ['user1', 'user2', 'admin']


def sign_up_by_django(request):
    info = ''
    #Users = Buyer.objects.all()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка на существование пользователя в базе данных
            if Buyer.objects.filter(name=username).exists():
                info = "Ошибка: пользователь уже существует."
            elif password != repeat_password:
                info = "Ошибка: пароли не совпадают."
            elif int(age) < 18:
                info = "Ошибка: возраст должен быть не менее 18 лет."
            else:

                # Создание нового пользователя

                Buyer.objects.create(name=username, balance=500.0, age=age)
                info = f"Приветствуем, {username}!"

    else:
        form = UserRegister()

    context = {'form': form, 'info': info}
    return render(request, 'registration_page.html', context)



def sign_up_by_html(request):
    Buyers = Buyer.objects.all()
    #print(Buyers)
    title = 'Главная'
    context = {
        'title': title,
    }
    users = ['alex', 'pops', 'oleg', 'pomidor']
    info = ''
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in [i.name for i in Buyers]:
                info = f'Приветствуем, {username}!'
                Buyer.objects.create(name=username, balance=500.0, age=age)

                context = {'form': form, 'info': info}
                return render(request, 'platform.html', context)

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in [i.name for i in Buyers]:
                info['error'] = 'Пользователь уже существует'


    else:
        form = UserRegister()
        info = f'Приветствуем, {username}!'

    context = {'form': form, 'info': info}
    return render(request, 'reg_page_html.html', context)  # Отображение шаблона