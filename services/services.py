import random

from lexicon.lexicon import LEXICON_RU


# Функция, возвращающая случайный выбор бота
def get_bot_choice() -> str:
    return random.choice(['heads_button', 'tails_button'])
