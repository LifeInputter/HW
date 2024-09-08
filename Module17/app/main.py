from fastapi import FastAPI
from app.routers import user
from app.routers import task

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)



'''
Задача "Основные маршруты":
Необходимо создать маршруты и написать Pydantic модели для дальнейшей работы.
Маршруты:
В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task', а также следующие маршруты, с пустыми функциями:
get '/' с функцией all_tasks.
get '/task_id' с функцией task_by_id.
post '/create' с функцией create_task.
put '/update' с функцией update_task.
delete '/delete' с функцией delete_task.
В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user', а также следующие маршруты, с пустыми функциями:
get '/' с функцией all_users.
get '/user_id' с функцией user_by_id.
post '/create' с функцией create_user.
put '/update' с функцией update_user.
delete '/delete' с функцией delete_user.
В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/', по которому функция возвращает словарь - {"message": "Welcome to Taskmanager"}.
Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI, объединив все маршруты в одно приложение.
Схемы:
Создайте 4 схемы в модуле schemas.py, наследуемые от BaseModel, для удобной работы с будущими объектами БД:
CreateUser с атрибутами: username(str), firstname(str), lastname(str) и age(int)
UpdateUser с атрибутами: firstname(str), lastname(str) и age(int)
CreateTask с атрибутами: title(str), content(str), priority(int)
UpdateTask с теми же атрибутами, что и CreateTask.
Обратите внимание, что 1/2 и 3/4 схемы обладают одинаковыми атрибутами.

Таким образом вы получите подготовленные маршруты и схемы для дальнейшего описания вашего API.

Примечания:
Запуск сервера осуществите командой python -m uvicorn main:app.

ВАЖНО: запуск uvicorn нужно осуществлять при условии, что main находится рядом с  app. Иначе будет ошибка 
Error loading ASGI app. Could not import module "main"
Пример: Users\Annam\PycharmProjects\Homeworks\Module17\аpp> python -m uvicorn main:app

'''