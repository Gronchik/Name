from Secure import bot_Token
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.webhook import get_new_configured_app

API_TOKEN = bot_Token
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBAPP_URL = f"https://{WEBAPP_HOST}:{WEBAPP_PORT}"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_PATH)


async def on_startup(dp):
    await bot.set_webhook(WEBAPP_URL + WEBHOOK_PATH)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_webhook(
        app,
        on_startup=on_startup,
        skip_updates=True
    )















# from Secure import bot_Token
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# # Настройки вебхука
# WEBHOOK_HOST = 'ЗДЕСЬ АДРЕС ИЗ NGROK'  # Адрес нашего сервера
# WEBHOOK_PATH = ''  # Путь до нашего api, где бот слушает сообщения
# WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'  # Адрес принятия запросов к боту
#
#
# # Настройка web-сервера
# WEBAPP_HOST = 'localhost'  # Хост нашего приложения (127.0.0.1 == localhost)
# WEBAPP_PORT = 8000  # Порт, на котором работает наше приложение
#
# # Инициализация бота и диспетчера
# bot = Bot(token=bot_Token)
# dp = Dispatcher(bot)
#
# # Создаем инлайн-клавиатуру с кнопкой "Кнопка 2" и указываем callback_data
# keyboard = InlineKeyboardMarkup()
# button2 = InlineKeyboardButton("Кнопка 2", callback_data="button2")
# keyboard.add(button2)
#
#
# # Обработчик для входящих запросов типа CallbackQuery
# @dp.callback_query_handler(lambda c: c.data == 'button2')
# async def process_callback_button2(callback_query: types.CallbackQuery):
#     # Извлекаем данные из callback_query
#     callback_data = callback_query.data
#
#     # Выполняем необходимые действия в ответ на нажатие кнопки
#     # Например, отправляем сообщение пользователю
#     await callback_query.answer(f'Предмет ubnfhf помещён в инвентарь')
#
#
# @dp.message_handler(lambda message: message.text.lower() == 'меню')
# async def menu(message: types.Message):
#     with open("images/Items/benzin.jpg", "rb") as photo_file:
#         await bot.send_photo(message.chat.id, photo_file, caption='Меню:', reply_markup=keyboard)
#
# # Обработчик для команды /start
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.answer("Привет! Я бот.", reply_markup=keyboard)
#
#
# @dp.message_handler(commands=['send_photo'])
# async def send_photo(message: types.Message):
#     # Отправляем текстовое сообщение
#     await message.answer("Вот ваше фото:")
#
#     # Отправляем фото вместе с текстом
#     with open("images/Items/benzin.jpg", "rb") as photo_file:
#         await bot.send_photo(message.chat.id, photo_file, caption="Подпись к фото")
#
#
# # Запуск бота
# if __name__ == '__main__':
#     from aiogram import executor
#
#     executor.start_polling(dp, skip_updates=True)
