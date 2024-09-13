from django.shortcuts import render
from  django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
users = ['Anton', 'Dianna','Archibald', 'Mary', 'alex', 'xxx']

#HTTP form
def sign_up_by_html(request):
    info ={}
    if request.method == "POST":
        #получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Repeat_password: {repeat_password}')
        print(f'Age: {age}')

        # Http ответ пользователю
        if username in users:
            error = 'Пользователь уже существует'
            info['ошибка'] = error
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')
        elif password != repeat_password:
            error = 'Пароли не совпадают'
            info['ошибка'] = error
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')
        elif int(age) < 18:
            error = 'Вы должны быть старше 18'
            info['ошибка'] = error
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')
        else:
            return HttpResponse(f'Приветствуем, {username}!')     # Http ответ пользователю

    context = {'info': info}
    return render(request, 'registration_page.html', context)

#Django forms
def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            #Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                error = 'Пользователь уже существует'
                info['ошибка'] = error
                for key, value in info.items():
                    if value == error:
                        return HttpResponse(f'{key}: {value}')
            elif password != repeat_password:
                error = 'Пароли не совпадают'
                info['ошибка'] = error
                for key, value in info.items():
                    if value == error:
                        return HttpResponse(f'{key}: {value}')
            elif age < 18:
                error = 'Вы должны быть старше 18'
                info['ошибка'] = error
                for key, value in info.items():
                    if value == error:
                        return HttpResponse(f'{key}: {value}')
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
        return render(request, 'registration_page.html', {'form': form})

