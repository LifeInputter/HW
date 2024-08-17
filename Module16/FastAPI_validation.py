from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# @app.get("/main")
# async def welcome() -> dict:
#     return {"message": "Главная страница"}
@app.get("/")  # get запрос - это адрес в строке, пишется обычно со знака ?переменная=значение
async def welcome() -> dict:  # ф-я выводит главную стр, данные тянет из словаря
    return {"message": "Главная страница"}


# запуск app из терминала: python3 -m uvicorn main:app
# uvicorn Module16.main:app --reload
# NB!при построении маршрутизации нужно сроблюдать порядок:от частного к общему (частное должно быть всегда выше располагаться)
'''
Создайте маршрут к странице администратора-"/user/admin". По нему должно выводиться сообщение "Вы вошли как администратор".
'''


@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}


'''
Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}". По нему должно выводиться
 сообщение "Вы вошли как пользователь № <user_id>".
 upd 16.2
 написать следующую валидацию:
Должно быть целым числом
Ограничено по значению: больше или равно 1 и меньше либо равно 100.
Описание - 'Enter User ID'
Пример - '1' 
'''


@app.get("/user/{user_id}")
async def user_path(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="10")]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


# ge - Не менее, le - не более


'''
Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user". По нему должно 
выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
upd 16.2
user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username и age, для которых необходимо написать следующую валидацию:
username - строка, age - целое число.
username ограничение по длине: больше или равно 5 и меньше либо равно 20.
age ограничение по значению: больше или равно 18 и меньше либо равно 120.
Описания для username и age - 'Enter username' и 'Enter age' соответственно.
Примеры для username и age
'''


@app.get("/user/{username}/{age}")
async def user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Sandman")],
        age: int = Path(ge=18, le=120, description="Enter age", example="33")) -> dict:
    return {"User": f'Информация о пользователе: Имя:{username}, возраст:{age}'}

# на тестовой веб-странице ввод имени пользователя и возраста в адр.строке будет выглядить как .../user?username=Alex&age=41
# http://127.0.0.1:8000/user?username=Alex&age=41
# вывод на самой странице: "Информация о пользователе: Имя:Alex, возраст:41"
