from fastapi import FastAPI

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
'''


@app.get("/user/{user_id}")
async def user_path(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


'''
Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user". По нему должно 
выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
'''

@app.get("/user")
async def user_info(username: str, age: int) -> dict:
    return {"User": f'Информация о пользователе: Имя:{username}, возраст:{age}'}

#на тестовой веб-странице ввод имени пользователя и возраста в адр.строке будет выглядить как .../user?username=Alex&age=41
# http://127.0.0.1:8000/user?username=Alex&age=41
# вывод на смой странице: "Информация о пользователе: Имя:Alex, возраст:41"