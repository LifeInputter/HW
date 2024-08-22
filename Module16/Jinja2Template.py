from fastapi import FastAPI, status, Body, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {'request': request, "users": users})


@app.get("/users/{user_id}")
async def get_users(request: Request, user_id: Annotated[int, Path(ge=1, le=100)]) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(description="Enter username", min_length=5, max_length=20, example="UrbanUser")],
        age: Annotated[int, Path(description="Enter yor age", ge=18, le=100, example=22)]
):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

    # new_id = str(int(max(users, key=int)) + 1)
    # users.append(new_id)
    # new_id = str(int(max(users, key=int)) + 1)
    # users[new_id] = f'Имя:{username}, возраст:{age}'
    # return f'User {new_id} is registered'


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(description='Enter User ID', ge=1, le=100, example=1)],
        username: Annotated[str, Path(description="Enter username", min_length=5, max_length=20, example="UrbanProfi")],
        age: Annotated[int, Path(description="Enter yor age", ge=18, le=100, example=22)]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(description='Enter User ID', ge=1, le=100, example=2)]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
        # f'User {user_id} has been deleted'
    raise HTTPException(status_code=404, detail="User was not found")

    # user_id = str(user_id)
    # if user_id in users:
    #     try:
    #         del users[user_id]
    #         return f'User {user_id} has been deleted'
    #     except IndexError:
    #         HTTPException(status_code=404, detail="User was not found")


'''
Цель: научиться взаимодействовать с шаблонами Jinja 2 и использовать их в запросах.

Задача "Список пользователей в шаблоне":
Подготовка:
Используйте код из предыдущей задачи (16.4).
Скачайте заготовленные шаблоны для их дополнения.
Шаблоны оставьте в папке templates у себя в проекте.
Создайте объект Jinja2Templates, указав в качестве папки шаблонов - templates.
Измените и дополните ранее описанные CRUD запросы:
Напишите новый запрос по маршруту '/':
Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и список users. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
Измените get запрос по маршруту '/users' на '/users/{user_id}':
Функция по этому запросу теперь принимает аргумент request и user_id.
Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и одного из пользователей - user. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
Создайте несколько пользователей при помощи post запроса со следующими данными:
username - UrbanUser, age - 24
username - UrbanTest, age - 22
username - Capybara, age - 60
В шаблоне 'users.html' заготовлены все необходимые теги и обработка условий, вам остаётся только дополнить закомментированные строки вашим Jinja 2 кодом (использование полей id, username и age объектов модели User):
1. По маршруту '/' должен отображаться шаблон 'users.html' со списком все ранее созданных объектов:
2. Здесь каждая из записей является ссылкой на описание объекта, информация о котором отображается по маршруту '/users/{user_id}':

'''
