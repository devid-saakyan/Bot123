from time import sleep

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext

from data.config import my_token
# from keyboard.inlinekeyboard import inlinkeyboard
from Utils.set_bot_commands import set_default_commands

# Память
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.redis import RedisStorage2

### Клавиатуры
from keyboard.inlinekeyboard.implementer import *
from keyboard.inlinekeyboard.customer_keyboard import *
# from DataBase import add_to_database_customers
from aiogram.dispatcher.filters.state import State, StatesGroup

from users.support import *
from keyboard.inlinekeyboard.support import *
from loader import bot, dp

async def on_startup(dp):
    await set_default_commands(dp)


class Customer(StatesGroup):
    question1 = State()
    question2 = State()


# bot = Bot(token=my_token)
# # dp = Dispatcher(bot)
# # dp = Dispatcher(bot, storage=RedisStorage2())
# dp = Dispatcher(bot, storage=MemoryStorage())

global a, b










'''''
#### Снизу код для клавиши Back 
'''''


@dp.callback_query_handler(lambda c: c.data == 'back1')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы вернулись в главное меню. Выберите : ',
                           reply_markup=inlinkeyboard())


@dp.callback_query_handler(lambda c: c.data == 'back2')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы вернулись к выбору направления. Выберите : ',
                           reply_markup=customer_keyboard1())


@dp.callback_query_handler(lambda c: c.data == 'back3')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы вернулись к выбору даты. Выберите : ',
                           reply_markup=customer_keyboard_data())


'''''
#### Сверху код для клавиши Back 
'''''


# @dp.callback_query_handlers(funk = lambda c: c.data and c.data.startswith('button_1'))
@dp.callback_query_handler(lambda c: c.data == 'button_1')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Меню для исполнителя:', reply_markup=inlinkeyboard_2())


@dp.callback_query_handler(lambda c: c.data == 'button_2')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Меню для заказчика:', reply_markup=customer_keyboard1())


@dp.callback_query_handler(lambda c: c.data == 'button_3')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваши работы:', reply_markup=inlinekeyboard_3())


@dp.callback_query_handler(lambda c: c.data == 'button_4')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите профессиональное ориентирование или '
                                                        'выберите список работ которые можно '
                                                        'взять :', reply_markup=inlinekeyboard_4())


@dp.callback_query_handler(lambda c: c.data == 'button_5')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Информация по Вашему профилю:')


@dp.message_handler(commands=['start', 'начать'])
async def send_hello(message: types.message):
    await message.answer(f'Здравствуйте , {message.from_user.full_name}!\n'
                         f'Задача этого сервиса -  помогать студентам и школьникам в учебе.\n'
                         f'Выполнение контрольных, задач, курсовых, рефератов и других заданий.\n'
                         f'Задания будут выполнять живые люди, а это значит, '
                         f'что преподаватель не сможет обвинить вас в списывании из интернета.\n'
                         f'Так же вы сможете самостоятельно выбирать себе помощника и договариваться с ним о стоимости работы.\n'
                         f'Или же стать помощником для кого-либо.\n'
                         f'Учитесь и зарабатывайте вместе с нами! '
                         , reply_markup=inlinkeyboard())


'''
### Снизу код для ЗАКАЗЧИКА (подборка предмета)
'''

'''
#### Здесь идёт подборка даты
'''


@dp.callback_query_handler(lambda c: c.data == 'customer_button_7')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вариант как можно скорее!')
    await bot.send_message(callback_query.from_user.id, 'Выберите ожидаемую стоимость 💰:',
                           reply_markup=customer_keyboard3_price())
    global data
    data = 0


@dp.callback_query_handler(lambda c: c.data == 'customer_button_8')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вариант 1-2 дня!')
    await bot.send_message(callback_query.from_user.id, 'Выберите ожидаемую стоимость 💰:',
                           reply_markup=customer_keyboard3_price())
    global data
    data = 2


@dp.callback_query_handler(lambda c: c.data == 'customer_button_9')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вариант 1-2 дня!')
    await bot.send_message(callback_query.from_user.id, 'Выберите ожидаемую стоимость 💰:',
                           reply_markup=customer_keyboard3_price())
    global data
    data = 4


@dp.callback_query_handler(lambda c: c.data == 'customer_button_10')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вариант в течение 7 дней!')
    await bot.send_message(callback_query.from_user.id, 'Выберите ожидаемую стоимость 💰:',
                           reply_markup=customer_keyboard3_price())
    global data
    data = 7


@dp.callback_query_handler(lambda c: c.data == 'customer_button_9')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы решили ввести дату сами!')
    await bot.send_message(callback_query.from_user.id, 'Выберите ожидаемую стоимость 💰:',
                           reply_markup=customer_keyboard3_price())
    await Customer.question1.set()


'''
#### Сверхут идёт подборка даты
'''

'''
#### Снизу идёт подборка цен
'''


@dp.callback_query_handler(lambda c: c.data == 'button_customer_1_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 100 рублей')
    global price
    price = 100


@dp.callback_query_handler(lambda c: c.data == 'button_customer_2_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 200 рублей')
    global price
    price = 200


@dp.callback_query_handler(lambda c: c.data == 'button_customer_3_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 300 рублей')
    global price
    price = 300


@dp.callback_query_handler(lambda c: c.data == 'button_customer_4_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 400 рублей')
    global price
    price = 400


@dp.callback_query_handler(lambda c: c.data == 'button_customer_5_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 500 рублей')
    global price
    price = 500


@dp.callback_query_handler(lambda c: c.data == 'button_customer_6_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 600 рублей')
    global price
    price = 600


@dp.callback_query_handler(lambda c: c.data == 'button_customer_7_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 700 рублей')
    global price
    price = 700


@dp.callback_query_handler(lambda c: c.data == 'button_customer_8_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 800 рублей')
    global price
    price = 800


@dp.callback_query_handler(lambda c: c.data == 'button_customer_9_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 900 рублей')
    global price
    price = 900


@dp.callback_query_handler(lambda c: c.data == 'button_customer_10_price')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 1000 рублей')
    global price
    price = 1000


'''
#### Сверху идёт подборка цен
'''


@dp.callback_query_handler(lambda c: c.data == 'customer_button_1')  # customer_button_1
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(callback_query.from_user.id, 'Вы выбрали гуманитария: ')
    await bot.send_message(callback_query.from_user.id,
                           'Вы выбрали гуманитарий! Укажите ожидаемое время исполнения заказа ⏳: ',
                           reply_markup=customer_keyboard_data())
    global a
    await Customer.question1.set()
    a = 'Гуманитарий'


@dp.callback_query_handler(lambda c: c.data == 'customer_button_2')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Программиста :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',
                           reply_markup=customer_keyboard_data())
    global a
    await Customer.question1.set()
    a = 'Программист'


@dp.callback_query_handler(lambda c: c.data == 'customer_button_3')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Юриста :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',
                           reply_markup=customer_keyboard_data())
    await Customer.question1.set()
    global a
    a = 'Юрист'


@dp.callback_query_handler(lambda c: c.data == 'customer_button_4')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Технаря :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',
                           reply_markup=customer_keyboard_data())
    global a
    await Customer.question1.set()
    a = 'Технарь'


@dp.callback_query_handler(lambda c: c.data == 'customer_button_5')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Естественника :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',
                           reply_markup=customer_keyboard_data())
    global a
    a = 'Естественник'
    await Customer.question1.set()


@dp.callback_query_handler(lambda c: c.data == 'customer_button_6')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Экономиста :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',
                           reply_markup=customer_keyboard_data())
    await Customer.question1.set()
    global a
    a = 'Экономист'


'''
### Сверху код для ЗАКАЗЧИКА (подборка предмета)
'''


@dp.message_handler(state=Customer.question1)  ### первое состояние
async def send_text(message: types.message, state: FSMContext):
    await message.answer('Укажите ожидаемое время исполнения заказа: ', reply_markup=customer_keyboard_data())
    answer = message.text
    global data
    data = answer
    await state.update_data(answer1=answer)
    await message.answer('Вот Ваша дата: {}'.format(answer))  # (state.get_data())
    # sleep(1)
    await message.answer('Введите желаемую стоимость: ', reply_markup=customer_keyboard3_price())

    await Customer.next()


@dp.message_handler(state=Customer.question2)  ## Состояние второе (вводим приблизительную стоимость)
async def send_text(message: types.message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')
    await message.answer('Вот Ваша стоимость: {} {}'.format(answer1, answer2))
    await message.answer('Вот Ваше имя: {}\n'
                         'Вот Ваш Chat_id{}\n'
                         'Вот Ваш предмет{}\n'
                         'Вот Ваши сроки исполнения заказа(в днях){}\n'
                         '{}\n')
    await state.finish()


'''
#### СНИЗУ Общение через бота 
'''
### Как я могу увидеть свой id
### Как я могу извлечь чужой id

# chat_id1 = 484050440  # Я
# chat_id2 = 492075107
# chat_id3 = 651741256   # Другой акк
#
# chat_id4 = 931180948 # Мама
#
# dialog1 = []
# dialog2 = []
# dialog3 = []


# @dp.message_handler()
# async def first_function(message):
#     if message.from_user.id == chat_id1:
#         # if message.text == 'show':
#         print('Слова Димы {}\n Слова Егора{}\n Слова акка{}\n'
#                   .format(dialog1, dialog2, dialog3))
#         dialog1.append(message.text)
#         await bot.send_message(chat_id2, message.text)
#         await bot.send_message(chat_id3, message.text)
#     elif message.from_user.id == chat_id2:
#         print('Слова Димы {}\n Слова Егора{}\n Слова акка{}\n'
#                   .format(dialog1, dialog2, dialog3))
#         dialog2.append(message.text)
#         await bot.send_message(chat_id1, message.text)
#         await bot.send_message(chat_id3, message.text)
#     elif message.from_user.id == chat_id3:
#         print('Слова Димы {}\n Слова Егора{}\n Слова акка{}\n'
#                   .format(dialog1, dialog2, dialog3))
#         dialog3.append(message.text)
#         await bot.send_message(chat_id1, message.text)
#         await bot.send_message(chat_id2, message.text)


'''
#### СВЕРХУ Общение через бота 
'''

# @dp.message_handler()
# async def first_function(message):
#     if message.from_user.id == chat_id1:
#         # if message.text == 'show':
#         dialog1.append(message.text)
#         print('Слова Димы {}'
#                   .format(dialog1, dialog2, dialog3))
#         await bot.send_message(chat_id4, message.text)
#         await bot.send_message(chat_id3, message.text)
#     elif message.from_user.id == chat_id4:
#         dialog2.append(message.text)
#         print('Слова Мамы{}\n'
#                   .format(dialog2, dialog2, dialog3))
#         await bot.send_message(chat_id1, message.text)
#         await bot.send_message(chat_id3, message.text)
#     elif message.from_user.id == chat_id3:
#         dialog3.append(message.text)
#         print('Слова Димы {}\n Слова Мамы{}\n Слова акка{}\n'
#                   .format(dialog1, dialog2, dialog3))
#         await bot.send_message(chat_id1, message.text)
#         await bot.send_message(chat_id4, message.text)


executor.start_polling(dp, on_startup=on_startup)
# executor.start_polling(dp, on_shutdown=True)
