from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import my_token

bot = Bot(token=my_token)
dp = Dispatcher(bot, storage=MemoryStorage())