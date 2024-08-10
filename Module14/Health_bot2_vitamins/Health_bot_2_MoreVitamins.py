import sqlite3

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
import crud_functions
from crud_functions import *

api = config_texts.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data="calories")
button2 = InlineKeyboardButton(text="Формулы расчета", callback_data='formulas')
kb.add(button)
kb.add(button2)


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


#
@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer("Введи имя пользователя (только латинский алфавит)")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    # await message.answer("Введите погоняло пользователя (только латинский алфавит)")
    if is_included(message.text):
        await message.answer("Пользователь существует, введи другое имя")
        await RegistrationState.username.set()
    else:
        await message.answer("Введи свой email")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введи свой возраст")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    await message.answer('Поздраляем, ты успешно прошел регистрацию')
    dt = await state.get_data()
    crud_functions.add_user(dt['username'], dt['email'], dt['age'])

    await state.finish()


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
    for number in range(1, 5):
        await message.answer(f'Название: Product{number}| Описание: описание{number} | Цена: {number * 100}$')
        # for i, item in enumerate(products):
        with open(f'files/img_{number + 10}.jpg', 'rb') as photo:
            await message.answer_photo(photo)  # , f'Название: {item[1]}\nОписание: {item[2]}\nЦена: {item[3]}$'
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


@dp.message_handler(state=UserState.height)  # handler  реагирует на переданное состояние UserState.height
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
    crud_functions.initiate_db()
    connection = sqlite3.connect('prod.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES ("Product1", "Описание: витамин C", 100)')
    cursor.execute('INSERT INTO Products (title, description, price) VALUES ("Product2", "Описание: витамин B", 200)')
    cursor.execute('INSERT INTO Products (title, description, price) VALUES ("Product3", "Описание: витамин A", 300)')
    cursor.execute('INSERT INTO Products (title, description, price) VALUES ("Product4", "Описание: витамин E", 400)')

    connection.commit()
    connection.close()

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



------


Задача "Регистрация покупателей":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.

Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число (не пустой)
balance - целое число (не пустой)
add_user(username, email, age), которая принимает: имя пользователя, почту и возраст. Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными. Баланс у новых пользователей всегда равен 1000. Для добавления записей в таблице используйте SQL запрос.
is_included(username) принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users, в противном случае False. Для получения записей используйте SQL запрос.

Изменения в Telegram-бот:
Кнопки главного меню дополните кнопкой "Регистрация".
Напишите новый класс состояний RegistrationState с следующими объектами класса State: username, email, age, balance(по умолчанию 1000).
Создайте цепочку изменений состояний RegistrationState.
Фукнции цепочки состояний RegistrationState:
sing_up(message):
Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
После ожидать ввода возраста в атрибут RegistrationState.username при помощи метода set.
set_username(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
Функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text. Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя" и запрашивать новое состояние для RegistrationState.username.
set_email(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
Далее выводить сообщение "Введите свой возраст:":
После ожидать ввода возраста в атрибут RegistrationState.age.
set_age(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users при помощи ранее написанной crud-функции add_user.
В конце завершать приём состояний при помощи метода finish().
'''
