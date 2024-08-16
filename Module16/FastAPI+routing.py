from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/main")               #get запрос - это адрес в строке, пишется обычно со знака ?переменная=значение
async def welcome() -> dict:    # ф-я выводит главную стр, данные тянет из словаря
    return {"message": "Главная страница"}

#запуск app из терминала: python3 -m uvicorn main:app