from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game, Phones
from django.contrib.auth.models import User
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    title = "Лучший сайт по продаже телефонов и игр"
    main = "Главная страница"
    link1 = "Регистрация"
    context = {

        'title': title,
        'main': main,
        'link1': link1

    }
    return render(request, 'platform.html', context)

def games(request):
    best_games = "Лучшие игры:"
    buy = "Купить"
    games = Game.objects.all()
    context = {
        'best_games': best_games,
        'buy': buy,
        'games': games
    }
    return render(request, 'games_list.html', context)



def phones(request):
    best_choice = "Список лучших смартфонов 2024:"
    phones_lst = ["Iphone 15 Pro", "Galaxy S24 Ultra", "Honor Magic 7 Pro"]
    buy = "Купить"
    phones = Phones.objects.all()
    context = {
        'best_choice': best_choice,
        'phones_lst': phones_lst,
        'buy': buy,
        'phones': phones
    }
    return render(request, 'phones.html', context)


def cart(request):
    title = "Корзина"
    img = "/static/Корзина.jpg"
    text1 = "Здесь ничего нет"
    context = {
        "title": title,
        "img": img,
        "text1": text1
    }
    return render(request, 'cart.html', context)


# HTTP form
def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        # получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Repeat_password: {repeat_password}')
        print(f'Age: {age}')

        # Http ответ пользователю
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            error = 'Пароли не совпадают'
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')
        elif age < '18':
            info['error'] = 'Вы должны быть старше 18'
            error = 'Вы должны быть старше 18'
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')

        elif Buyer.objects.filter(name=username).exists():
            error = 'Пользователь уже существует'
            info['error'] = 'Пользователь уже существует'
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')
        else:
            Buyer.objects.create(name=username, balance=0, age=age)
            info['message'] = f'Приветствуем, {username}!'
            return HttpResponse(f'Приветствуем, {username}!')

            # return redirect('platform/')

    context = {'info': info}
    return render(request, 'registration_page.html', context)


# Django forms
def sign_up_by_django(request):
    Users = Buyer.objects.all()
    usernames = [i.name for i in Users]
    i=0
    info = {'error':[]}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in usernames and password == repeat_password and int(age) >= 18:
                Buyer.objects.create(name=username, balance=0, age=age)
                context = {'username': username}
                return render(request, 'registration_complete.html')
              # return HttpResponse(f'Приветствуем, {username}!')

            elif username in usernames:
                i += 1
                info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                print(info[f'error {i}'])
                return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')

            elif password != repeat_password:
                i += 1
                info[f'error {i}'] = HttpResponse('Пароли не совпадают', status=400, reason='incorrect password')
                print(info[f'error {i}'])
                return HttpResponse('Пароли не совпадают', status=400, reason='incorrect password')

            elif int(age) < 18:
                i += 1
                info[f'error {i}'] = HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')
                print(info[f'error {i}'])
                return HttpResponse('Ваш возраст менее 18 лет', status=400, reason='insufficient age')


    else:
        form = UserRegister()
    context = {'info': info, 'form': form}
    return render(request, 'registration_page.html', context)
