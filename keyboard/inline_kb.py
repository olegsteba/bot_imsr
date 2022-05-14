from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_buttons = [
    ('Все задачи', 'all_task'), 
    ('Текст задания по id', 'text_task'),
    ('Новое задание', 'last_task'), 
    ('Отправить решение', 'send_result'),
]

kb1 = InlineKeyboardMarkup(row_width=1)
kb1.add(*[InlineKeyboardButton(i, callback_data=f"mb-{j}") for i, j in main_buttons])


