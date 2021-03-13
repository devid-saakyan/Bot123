import telebot
from data.config import my_token
from my_sql import add_to_database
from filters import recognize_name

token = my_token

bot = telebot.TeleBot(token)

def keyboard():

    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('1-ая кнопка')
    button2 = telebot.types.InlineKeyboardButton('2-ая кнопка')
    markup.add(button1, button2)
    return markup
@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = str(message.chat.id)
    first_name = str(message.chat.first_name)
    last_name = str(message.chat.last_name)
    username = str(message.chat.username)

    name = recognize_name(first_name,last_name, username, chat_id)
    bot.send_message(chat_id, 'Приветствуем Вас {} !в нашем боте'.
                     format(name), disable_web_page_preview = True, reply_markup=keyboard())

@bot.message_handler(content_types=["text"])
def function_for_text(message):
    chat_id = str(message.chat.id)
    username = str(message.chat.username)
    first_name = str(message.chat.first_name)
    last_name = str(message.chat.last_name)
    text = str(message.text)

    name = recognize_name(first_name, last_name, username, chat_id)
    if text == '1-ая кнопка':
        bot.send_message(chat_id, text='Моё имя {} Вы нажали кнопку 1'.format(name))
        print(chat_id, username, first_name, last_name)

        add_to_database(chat_id, name)

bot.polling()