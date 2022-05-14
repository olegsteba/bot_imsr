import asyncio
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, admin_id
from aiogram.dispatcher.filters.state import State, StatesGroup

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO
)

storage = MemoryStorage()

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

# создаём форму и указываем поля
class TaskText(StatesGroup):
    task_id = State() 

    

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Не флуди...")

async def set_default_commands(dp):
    await bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("menu", "Меню"),
    ])
    
async def on_startup(dp):
    await set_default_commands(dp)
    print("Бот запущен!")    
    # await bot.send_message(chat_id=admin_id, text=f"bot_started")


if __name__ == "__main__":
    from handlers.commands import dp
    executor.start_polling(dp, on_startup=on_startup)
    import handlers