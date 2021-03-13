from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

items = ['Программист', 'Юрист', 'Экономист', 'Естественник', 'Гуманитарий', 'Технарь']
prices = ['400-600', '600-800', '800-1000', 'Произвольная сумма']

class Customer(StatesGroup):
    waiting_for_items = State()
    waiting_for_price = State()

async def customer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in items:
        keyboard.add(item)
    await message.answer('Выберите напрвление: ', reply_markup=keyboard)
    await Customer.waiting_for_items.set()

async def customer_2(message: types.Message, state: FSMContext):
    if message.text.lower() not in items:
        await message.answer('Пожалуйста, выберите направление, используя клавиатуру ниже.')
        return
    await state.update_data() # Что сюда нужно передавать?

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for price in prices:
        keyboard.add(price)
    await Customer.next() # await Customer.waiting_for_price.set()
    await message.answer("Выберите цену: ", reply_markup=keyboard)

async def price_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in prices:
        await message.answer("Пожалуйста, укажите цену, используя клавиатуру ниже.")
        return
    user_data = await state.get_data()
    await message.answer(f"Вы выбрали предмет {message.text.lower()} и цену {user_data['chosen_food']}.\n"
                         f"Попробуйте теперь сделать новый заказ: /new_order", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()

def register_handlers_customer(dp: Dispatcher):
    dp.register_message_handler(customer, )  # Как наследовать, после нажатия на кнопку "меню для заказчика"