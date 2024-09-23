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
    title = "Мобильные устройства"
    phones_lst = "Список лучших смартфонов 2024:"
    context = {
        'title': title,
        'phones_lst': phones_lst
    }
    return render(request,'phones.html', context)

def cart(request):
    return render(request,'cart.html')

