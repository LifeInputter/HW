from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

import config_texts
from config_texts import *
from kb import *

api = config_texts.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data="calories")
button2 = InlineKeyboardButton(text="Формулы расчета", callback_data='formulas')
kb.add(button)
kb.add(button2)


# start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
# start_button = KeyboardButton(text='Информация')
# start_button2 = KeyboardButton(text="Рассчитать")
# buy_button = KeyboardButton(text="Купить")
# start_kb.add(start_button)
# start_kb.add(start_button2)
# start_kb.add(buy_button)


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


#
@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выбери опцию", reply_markup=kb)


@dp.message_handler(commands=['start'])  # этот хэндлер реагирует на команду старт
async def start_message(message):
    print('Привет! Я бот, помогающий твоему здоровью.')
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=start_kb)


@dp.message_handler(text="Информация")
async def info(message):
    await message.answer("Если ты думаешь о крепком здоровье, я помогу тебе с витаминами")


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    await message.answer(config_texts.product1)
    with open('files/C_vit.jpg', 'rb') as img1:
        await message.answer_photo(img1)
    await message.answer(config_texts.product2)
    with open("files/B_vit.jpg", "rb") as img2:
        await message.answer_photo(img2)
    await message.answer(config_texts.product3)
    with open("files/A_vit.jpg", 'rb') as img3:
        await message.answer_photo(img3)
    await message.answer(config_texts.product4)
    with open("files/E_vit.jpg", 'rb') as img4:
        await message.answer_photo(img4)

    await message.answer(text='Выберите продукт для покупки', reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(config_texts.confirm)
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n'
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(
    text=["calories", "Calories"])  # message_handler, который реагирует на текстовое сообщение / кнопку 'Рассчитать'
async def set_age(call):  # Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:
    await call.message.answer("Введи свой возраст")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)  # Эта функция должна обновлять данные в состоянии age на message.text
async def set_height(message, state):  # (написанное пользователем сообщение). Используйте метод update_data.
    await state.update_data(ag=message.text)
    await message.answer("Введи свой рост")
    await UserState.height.set()


@dp.message_handler(state=UserState.height)  # hadler  реагирует на переданное состояние UserState.height
async def set_weight(message, state):  # эта ф-я обновляет данные в состоянии height на message.text от пользователя
    await state.update_data(hei=message.text)
    await message.answer("Введи свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(wei=message.text)
    data = await state.get_data()
    calories = 10 * float(data['wei']) + 6.25 * float(data['hei']) - 5 * float(data['ag']) + 5
    await message.answer(f'Твоя норма калорий по формуле Миффлина - Сан Жеора: {calories}')

    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

'''
Задача "Цепочка вопросов"+

НЗадача "Ещё больше выбора":
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
С текстом 'Рассчитать норму калорий' и callback_data='calories'
С текстом 'Формулы расчёта' и callback_data='formulas'
Создайте новую функцию main_menu(message), которая:
Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
Создайте новую функцию get_formulas(call), которая:
Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
Будет присылать сообщение с формулой Миффлина-Сан Жеора.
Измените функцию set_age и декоратор для неё:
Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
По итогу получится следующий алгоритм:
Вводится команда /start
На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
'''
