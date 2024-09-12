from django.shortcuts import render

# Create your views here.
def platform(request):
    title = "Лучший сайт по продаже телефонов"
    main = "Главная страница"
    context = {
        'title': title,
        'main': main
    }
    return render(request, 'platform.html', context)


def phones(request):
    best_choice = "Список лучших смартфонов 2024:"
    phones_lst = ["Iphone 15 Pro", "Galaxy S24 Ultra", "Honor Magic 7"]
    buy = "Купить"
    context = {
        'best_choice': best_choice,
        'phones_lst': phones_lst,
        'buy': buy
    }
    return render(request,'phones.html', context)

def cart(request):
    title = "Корзина"
    img = "/static/Корзина.jpg"
    text1 = "Здесь ничего нет"
    context = {
        "title":title,
        "img": img,
        "text1": text1
    }
    return render(request,'cart.html', context)

