import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, inline_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

import logging
import config
import db_log

api = config.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup(row_width=3)
button1 = InlineKeyboardButton(text='Да, +100 единиц тебе в карму!', callback_data='back')
button2 = InlineKeyboardButton(text="Нет, пойду спрошу у яндекса", url="https://ya.ru")
kb.add(button1)
kb.add(button2)
db_log.init_db(force=True) # True - пересоздает БД кадый раз False - последовательно добавляет все записи


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # db_log.add_message()
    # await bot.send_message(f'Привет, @{message.from_user.username}!\n\n', reply_markup=start_kb)
    await message.answer(f'Привет, @{message.from_user.username}!\n\n Что тебя интересует, спроси меня)')


@dp.callback_query_handler(text='back')
async def back(call):
    await call.message.answer(f'Ок, что еще тебя интересует, спроси меня)')
    await call.answer()


@dp.message_handler(content_types=['text'])
async def text(message):
    db_log.add_message(user_id=message.from_user.id, text=message.text )
    url = 'https://ru.wikipedia.org/w/index.php?search=' + message.text
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    links = soup.find_all("div", class_="mw-search-result-heading")
    if len(links) > 0:
        url = "https://ru.wikipedia.org" + links[0].find("a")["href"]

    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(option)
    driver.get(url)

    driver.execute_script("window.scrollTo(0,200)")
    driver.save_screenshot('img.png')
    driver.close()

    photo = open('img.png', 'rb')
    await message.answer_photo(photo)
    await message.answer(f'Ссылка на статью: {url}')
    await message.answer("Нашел нужный результат?", reply_markup=kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
