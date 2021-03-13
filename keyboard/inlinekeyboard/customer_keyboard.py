from aiogram import types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Start

def inlinkeyboard():
    markup = InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_1 = InlineKeyboardButton('Исполнитель', callback_data='button_1')
    button_2 = InlineKeyboardButton('Заказчик', callback_data='button_2')
    button_6_admin = types.InlineKeyboardButton('Связь с админом', callback_data='button_6', url='https://t.me/i_Tele_2')
    markup.add(button_1, button_2)
    markup.row(button_6_admin)
    return markup

def customer_keyboard1():    #########     клавы для предметов
    markup = InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_3 = InlineKeyboardButton('Гуманитарий', callback_data='customer_button_1')
    button_4 = InlineKeyboardButton('Программист', callback_data='customer_button_2')
    button_5 = InlineKeyboardButton('Юрист', callback_data='customer_button_3')
    button_6 = InlineKeyboardButton('Технарь', callback_data='customer_button_4')
    button_7 = InlineKeyboardButton('Естественник', callback_data='customer_button_5')
    button_8 = InlineKeyboardButton('Экономист', callback_data='customer_button_6')
    button_9 = InlineKeyboardButton('⬅ Назад', callback_data='back1')
    button_6_admin = types.InlineKeyboardButton('Связь с админом', callback_data='button_6',
                                                url='https://t.me/i_Tele_2')
    markup.add(button_3, button_4, button_5, button_6, button_7, button_8)
    markup.row(button_9)
    markup.row(button_6_admin)
    return markup

def customer_keyboard_data():
    markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_customer_1 = types.InlineKeyboardButton('Как можно скорее', callback_data='customer_button_7')
    button_customer_2 = types.InlineKeyboardButton('1-2 дня', callback_data='customer_button_8')
    button_customer_3 = types.InlineKeyboardButton('2-4 дня', callback_data='customer_button_9')
    button_customer_4 = types.InlineKeyboardButton('в течение 7 дней', callback_data='customer_button_10')
    button_customer_5 = types.InlineKeyboardButton('ввести свой срок исполнения', callback_data='customer_button_11')
    button_customer_6 = InlineKeyboardButton('⬅ Назад', callback_data='back2')
    button_6_admin = types.InlineKeyboardButton('Связь с админом', callback_data='button_6',
                                                url='https://t.me/i_Tele_2')
    markup.add(button_customer_1, button_customer_2, button_customer_3, button_customer_4, button_customer_5,)
    markup.row(button_customer_6)
    markup.row(button_6_admin)
    return markup

def customer_keyboard3_price():
    markup = types.InlineKeyboardMarkup(resize_keyboard=True, selective=True)
    button_customer_1 = types.InlineKeyboardButton('100руб', callback_data='button_customer_1_price')
    button_customer_2 = types.InlineKeyboardButton('200руб', callback_data='button_customer_2_price')
    button_customer_3 = types.InlineKeyboardButton('300руб', callback_data='button_customer_3_price')
    button_customer_4 = types.InlineKeyboardButton('400руб', callback_data='button_customer_4_price')
    button_customer_5 = types.InlineKeyboardButton('500руб', callback_data='button_customer_5_price')
    button_customer_6 = types.InlineKeyboardButton('600руб', callback_data='button_customer_6_price')
    button_customer_7 = types.InlineKeyboardButton('700руб', callback_data='button_customer_7_price')
    button_customer_8 = types.InlineKeyboardButton('800руб', callback_data='button_customer_8_price')
    button_customer_9 = types.InlineKeyboardButton('900руб', callback_data='button_customer_9_price')
    button_customer_10 = types.InlineKeyboardButton('1000руб', callback_data='button_customer_10_price')
    button_customer_11 = InlineKeyboardButton('⬅ Назад', callback_data='back3')
    button_6_admin = types.InlineKeyboardButton('Связь с админом', callback_data='button_6',
                                                url='https://t.me/i_Tele_2')
    markup.add(button_customer_1, button_customer_2, button_customer_3, button_customer_4, button_customer_5,
               button_customer_6, button_customer_7, button_customer_8, button_customer_9, button_customer_10)
    markup.row(button_customer_11)
    markup.row(button_6_admin)
    return markup
