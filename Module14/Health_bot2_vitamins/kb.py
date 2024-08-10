from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Информация"),
         KeyboardButton(text="Рассчитать")
        ],
        [KeyboardButton(text="Регистрация"),
         KeyboardButton(text='Купить')
         ]
        ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text='Продукт1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт2', callback_data="product_buying")],
        [InlineKeyboardButton(text="Продукт3", callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт4', callback_data='product_buying')]

    ]
)

