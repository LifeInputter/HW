from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text="Рассчитать")
kb.add(button)
kb.add(button2)


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(commands=['start'])  # этот хэндлер реагирует на команду старт
async def start_message(message):
    print('Привет! Я бот, помогающий твоему здоровью.')
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text="Информация")
async def info(message):
    await message.answer("Если ты думаешь о правильном питании, я помогу определить тебе норму калорий")


@dp.message_handler(
    text="Рассчитать")  # message_handler, который реагирует на текстовое сообщение / кнопку 'Рассчитать'
async def set_age(message):  # Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:
    await message.answer("Введи свой возраст", reply_markup=kb)
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
Задача "Цепочка вопросов":
Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.
Группа состояний:
Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
Создайте класс UserState наследованный от StateGroup.
Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).
Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов. Напишите следующие функции для обработки состояний:
Функцию set_age(message):
Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
Функцию set_growth(message, state):
Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
Эта функция должна обновлять данные в состоянии age на message.text (написанное пользователем сообщение). Используйте метод update_data.
Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
Функцию set_weight(message, state):
Оберните её в message_handler, который реагирует на переданное состояние UserState.growth.
Эта функция должна обновлять данные в состоянии growth на message.text (написанное пользователем сообщение). Используйте метод update_data.
Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
После ожидать ввода роста в атрибут UserState.weight при помощи метода set.
Функцию send_calories(message, state):
Оберните её в message_handler, который реагирует на переданное состояние UserState.weight.
Эта функция должна обновлять данные в состоянии weight на message.text (написанное пользователем сообщение). Используйте метод update_data.
Далее в функции запомните в переменную data все ранее введённые состояния при помощи state.get_data().
Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий (для женщин или мужчин - на ваше усмотрение). Данные для формулы берите из ранее объявленной переменной data по ключам age, growth и weight соответственно.
Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.
Финишируйте машину состояний методом finish().
!В течение написания этих функций помните, что они асинхронны и все функции и методы должны запускаться с оператором await.
'''
