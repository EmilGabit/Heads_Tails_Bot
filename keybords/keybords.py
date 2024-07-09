from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами орел, решка и отказа
heads_button = KeyboardButton(text=LEXICON_RU['heads_button'])
tails_button = KeyboardButton(text=LEXICON_RU['tails_button'])
no_button = KeyboardButton(text=LEXICON_RU['no_button'])
go_button = KeyboardButton(text=LEXICON_RU['go_button'])
letsgo = KeyboardButton(text=LEXICON_RU['letsgo'])

letsgo_builder = ReplyKeyboardBuilder()

letsgo_builder.row(letsgo, width=1)

letsgo_kb: ReplyKeyboardMarkup = letsgo_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Инициализируем билдер для клавиатуры с кнопками орел, решка и отказа
heads_tails_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
heads_tails_kb_builder.row(heads_button, tails_button, no_button, width=2)

# Создаем клавиатуру с кнопками орел, решка и отказа
heads_tails_kb: ReplyKeyboardMarkup = heads_tails_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Создаем инлайн кнопку с параметром callback_data
toss_button = InlineKeyboardButton(
    text=LEXICON_RU['letsgo'],
    callback_data= 'toss'
)
# Создаем объект инлайн-клавиатуры
toss = InlineKeyboardMarkup(
    inline_keyboard=[[toss_button]]
)

# Создаем объекты инлайн-кнопок url
url_button = InlineKeyboardButton(
    text='Перейти к просмотру видео',
    url='https://www.youtube.com/watch?v=oZWCWj1aNII'
)

# Создаем объект инлайн-клавиатуры url
keyboard_help = InlineKeyboardMarkup(
    inline_keyboard=[[url_button]]
)

# Инициализируем билдер для клавиатуры с кнопками
go_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
go_no_kb_builder.row(go_button, no_button, width=2)

# Создаем клавиатуру с кнопками Давай и Не хочу
go_no_kb: ReplyKeyboardMarkup = go_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

