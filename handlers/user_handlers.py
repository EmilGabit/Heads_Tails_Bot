from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keybords.keybords import heads_tails_kb, toss, keyboard_help, go_no_kb, letsgo_kb
from lexicon.lexicon import LEXICON_RU
from services.services import get_bot_choice
from aiogram.types import CallbackQuery
from date_base.date_base import users
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=heads_tails_kb)
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in_game': False,
            'choice': None,
            'heads': 0,
            'tails': 0,
            'total_choice': 0,
            'successfully': 0,
            'no_successfully' : 0
        }


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=keyboard_help)

# Этот хэндлер срабатывает на команду /stat
@router.message(Command(commands='stat'))
async def process_help_command(message: Message):
    await message.answer(f"{LEXICON_RU['choice']} {users[message.from_user.id]['choice']}\n"
                         f"{LEXICON_RU['total_choice']} {users[message.from_user.id]['total_choice']}\n"
                         f"{LEXICON_RU['successfully']} {users[message.from_user.id]['successfully']}\n"
                         f"{LEXICON_RU['no_successfully']} {users[message.from_user.id]['no_successfully']}\n",
                         reply_markup=go_no_kb
                         )


# Этот хэндлер срабатывает на нажатую кнопку Орел
@router.message(F.text == LEXICON_RU['heads_button'])
async def process_heads_answer(message: Message):
    if not users[message.from_user.id]['in_game'] :
        await message.answer(text=LEXICON_RU['letsgo_text'], reply_markup = letsgo_kb)
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['choice'] = LEXICON_RU['heads_button']
        users[message.from_user.id]['heads'] += 1
    else:
        await message.answer(f"Вы уже сделали свой выбор {users[message.from_user.id]}\n"
                             f"Нажмите на кнопку: \n",
                             reply_markup=letsgo_kb
                             )

# Этот хэндлер срабатывает на нажатую кнопку Решка
@router.message(F.text == LEXICON_RU['tails_button'])
async def process_tails_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer(text=LEXICON_RU['letsgo_text'], reply_markup = letsgo_kb)
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['choice'] = LEXICON_RU['tails_button']
        users[message.from_user.id]['tails'] += 1
    else:
        await message.answer(f"Вы уже сделали свой выбор {users[message.from_user.id]['choice']}\n"
                             f"Нажмите на кнопку: \n",
                             reply_markup=letsgo_kb
                             )

# Этот хэндлер срабатывает на нажатую кнопку Подбросить
@router.message(F.text == LEXICON_RU['letsgo'])
async def process_letsgo_answer(message: Message):
    choosing_a_bot = get_bot_choice()
    if users[message.from_user.id]['choice'] == LEXICON_RU[choosing_a_bot]:
        users[message.from_user.id]['in_game'] = False
        users[message.from_user.id]['total_choice'] += 1
        users[message.from_user.id]['successfully'] += 1
        await message.answer(text= LEXICON_RU['lucky'],
                             reply_markup = go_no_kb
                                     )
    else:
        users[message.from_user.id]['in_game'] = False
        users[message.from_user.id]['total_choice'] += 1
        users[message.from_user.id]['no_successfully'] += 1
        await message.answer(text=LEXICON_RU['no_lucky'],
                             reply_markup=go_no_kb
                             )

# Этот хэндлер срабатывает на отказ пользователя подбрасывать монетку
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])

# Этот хэндлер срабатывает на согласие пользователя подбрасывать монетку
@router.message(F.text == LEXICON_RU['go_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=heads_tails_kb)


# # Этот хэндлер срабатывает на любую из игровых кнопок
# @router.message(F.text.in_([LEXICON_RU['rock'],
#                             LEXICON_RU['paper'],
#                             LEXICON_RU['scissors']]))
# async def process_game_button(message: Message):
#     bot_choice = get_bot_choice()
#     await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
#                               f'- {LEXICON_RU[bot_choice]}')
#  #   winner = get_winner(message.text, bot_choice)
#     await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)