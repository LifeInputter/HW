from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Это страница"}
@app.get("/main")               #get запрос - это адрес в строке, пишется обычно со знака ?переменная=значение
async def welcome() -> dict:    # ф-я выводит главную стр, данные тянет из словаря
    return {"message": "Главная страница"}

#запуск app из терминала: python3 -m uvicorn main:app
#uvicorn Module16.main:app --reload
