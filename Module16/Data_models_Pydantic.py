from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


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
Цель: научиться описывать и использовать Pydantic модель.

Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
'''