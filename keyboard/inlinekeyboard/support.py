import random

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from telebot.types import InlineKeyboardButton

from data.config import support_ids, my_token

# from app import dp  # Это правильный импорт?  Что за метод .new в callback_data

bot = Bot(token=my_token)
dp = Dispatcher(bot, storage=MemoryStorage())

support_callback = CallbackData('ask_support', 'message', 'user_id', 'as_user')
cancel_support = CallbackData('cancel_support', 'user_id')

async def check_support_available(support_id):
    state = dp.current_state(chat=support_id, user=support_id)
    state_str = str(
        await state.get_state()
    )
    if state_str == "in_support":
        return
    else:
        return support_id

async def get_support_manager():
    random.shuffle(support_ids)
    for support_id in support_ids:
        support_id = await check_support_available(support_id)
        if support_id:
            return support_id
        else:
            return

async def support_keyboard(messages, user_id=None):
    if user_id:
        contact_id = int(user_id)
        as_user = "no"
        text = "Ответить пользователю"
    else:
        contact_id = get_support_manager()
        as_user = "yes"
        if messages == "many" and contact_id is None:
            return False
        elif messages == "one" and contact_id is None:
            contact_id = random.choice(support_ids)

        if messages == "one":
            text = "Написать 1 сообщение в техподдержку"
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text=text,
            callback_data=support_callback.new(
                messages=messages,
                user_id=contact_id,
                as_user=as_user
            )

        )
    )

    if messages == "many":
        keyboard.add(
            InlineKeyboardButton(
                text="Завершить сеанс",
                callback_data=cancel_support.new(
                    user_id=contact_id
                )
            )
        )
    return keyboard