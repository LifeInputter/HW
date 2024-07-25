from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


#
@dp.message_handler(text=['wtf', 'ff'])  # этот хэндлер перехватывает сообщения из списка
async def matreshka_message(message):
    print("Matre$$ka message")


@dp.message_handler(commands=['start'])  # этот хэндлер реагирует на команду старт
async def start_message(message):
    print('Привет! Я бот, помогающий твоему здоровью.')
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')


@dp.message_handler()  # этот хэндлер перехватывает абсолютно все сообщения
async def all_message(message):
    print("Введите команду /start, чтобы начать общение")
    await message.answer("Введите команду /start, чтобы начать общение")  #отправка ответа в чат телеграмм


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

'''''
Задача "Он мне ответил!":
Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.

'''''