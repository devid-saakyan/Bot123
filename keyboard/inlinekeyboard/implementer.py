from aiogram import types
# Клавиши
def keyboard():
    markup = types.KeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    button1 = types.KeyboardButton('Я заказчик')
    button2 = types.KeyboardButton('Я исполнитель')
    markup.add(button1, button2)
    return markup

# Start
def inlinkeyboard():
    markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_1 = types.InlineKeyboardButton('Исполнитель', callback_data='button_1')
    button_2 = types.InlineKeyboardButton('Заказчик', callback_data='button_2')
    markup.add(button_1, button_2)
    return markup
# Сообщение которое отправляется исполнителю первое Клавиатура для команды Исполнитель
def inlinkeyboard_2():
    markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_3 = types.InlineKeyboardButton('Ваши работы', callback_data='button_3')
    button_4 = types.InlineKeyboardButton('Найти работу', callback_data='button_4')
    button_5 = types.InlineKeyboardButton('Личный профиль', callback_data='button_5')
    button_6 = types.InlineKeyboardButton('Связь с админом', callback_data='button_6', url='https://t.me/i_Tele_2')
    markup.row(button_3, button_4, button_5) # Можно ли создать button_1 или он будет вызываться всегда
    markup.row(button_6)
    return markup

# Клавиатура для пункта Ваши работы
def inlinekeyboard_3():
    markup = types.InlineKeyboardMarkup(resize_keyboard=True, selective=True)
    button_7 = types.InlineKeyboardButton('Информация о заказе', callback_data='button_7')
    button_8 = types.InlineKeyboardButton('Ссылка на чат', callback_data='button_8')
    markup.add(button_7, button_8)
    return markup

# Клавиатура для пункта Найти работу
def inlinekeyboard_4():
    markup = types.InlineKeyboardMarkup(resize_keyboard=True, selective=True)
    button_9 = types.InlineKeyboardButton('Программист', callback_data='button_9')
    button_10 = types.InlineKeyboardButton('Юрист', callback_data='button_10')
    button_11 = types.InlineKeyboardButton('Экономист', callback_data='button_11')
    button_12 = types.InlineKeyboardButton('Естественник', callback_data='button_12')
    button_13 = types.InlineKeyboardButton('Гуманитарий', callback_data='button_13')
    button_14 = types.InlineKeyboardButton('Технарь', callback_data='button_14')
    button_15 = types.InlineKeyboardButton('Список работ', callback_data='button_15')
    markup.row(button_9, button_10, button_11)
    markup.row(button_12, button_13)
    markup.row( button_14, button_15)
    return markup
