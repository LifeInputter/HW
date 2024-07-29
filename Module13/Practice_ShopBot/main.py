import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from config import *
from keyboards import *
import texts

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}! ''\n' +texts.start, reply_markup = start_kb)

#message.answer_photo
#.answer_video
#.answer_file


@dp.message_handler(text ="О нас")
async def price(message):
    with open('files/rus2100.jpg', "rb") as img:
        await message.answer_photo(img, texts.about, reply_markup = start_kb)

@dp.message_handler(text = "Стоимость")
async def info(message):
    await message.answer("Что вас интересует", reply_markup = catalog_kb)

@dp.callback_query_handler(text = "medium")
async def buy_m(call):
    with open("files/kzn.jpg", "rb") as img:
        await call.message.answer_photo(img, texts.Mgame, reply_markup = buy_kb)
        await call.answer()

@dp.callback_query_handler(text = "big")
async def buy_l(call):
    with open("files/spb2100.jpg", 'rb') as img:
        await call.message.answer_photo(img, texts.Lgame, reply_markup = buy_kb)
        await call.answer()

@dp.callback_query_handler(text = "mega")
async def buy_xl(call):
    with open("files/vld2100.jpeg", 'rb') as img:
        await call.message.answer_photo(img, texts.XLgame, reply_markup = buy_kb)
        await call.answer()

@dp.callback_query_handler(text = "other")
async def buy_other(call):
    with open("files/art_pic3.jpg", 'rb') as img:
        await call.message.answer_photo(img, texts.other, reply_markup = buy_kb)
        await call.answer()

@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer("Что Вас интересует:", reply_markup=catalog_kb)
    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)