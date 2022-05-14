from email import message
from main import dp, bot, anti_flood, TaskText
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboard.inline_kb import kb1
from handlers.tasks import all_task, text_task
from asyncio import sleep



@dp.message_handler(commands=['start', 'help'])
async def start_command(msg: types.Message):
    try:
        return await msg.answer(text=f"Привет я Бот imsr!")
    except:
        await msg.reply("Общение через ЛС:\nhttps://t.me/SupOleBot")

@dp.message_handler(commands=['menu'])
async def menu_command(msg: types.Message):
    return await msg.answer("Выберите действие", reply_markup=kb1)

@dp.callback_query_handler(lambda x: x.data== 'mb-all_task')
async def handler_all_tasks(msg: types.CallbackQuery):
    text = ""
    tasks = await all_task()
    for task in tasks:
        text += f"#{task.get('id')}. {task.get('title')}\n"
    await bot.send_message(chat_id=msg.from_user.id, text=text)
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message.message_id)

@dp.callback_query_handler(lambda x: x.data== 'mb-text_task')
async def handler_text_task(msg: types.CallbackQuery):
    await TaskText.task_id.set()
    await bot.send_message(chat_id=msg.from_user.id, text="Номер задачи")
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message.message_id)
    

@dp.message_handler(lambda x: not x.text.isdigit(), state=TaskText.task_id)
async def process_task_id_invalid(msg: types.Message, state: FSMContext):
    await bot.send_message(
        chat_id=msg.from_user.id, 
        text=f"Необходимо ввести число"
    )
        
@dp.message_handler(lambda x: x.text.isdigit(), state=TaskText.task_id)
async def process_task_id(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['task_id'] = msg.text 
    task = await text_task(data['task_id'])
    await bot.send_message(
         chat_id=msg.from_user.id, 
         text=f"Задача № {data['task_id']}\n {task['description']}"
    )
    await state.finish()
