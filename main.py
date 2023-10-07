from Keyboards import menuKeyboard, mainMenuKeyboard
from Functions import stickerStats
from DBase import bdCheckId, bdPasteUser, bdChangeStats, bdStatistic
from Secure import bot_Token
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, types
from aiogram import executor

# Инициализация бота и диспетчера
bot = Bot(token=bot_Token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(Text(equals='меню', ignore_case=True))
async def menu(message: types.Message):
    with open("images/Items/Menu.jpg", "rb") as photo_file:
        await bot.send_photo(message.chat.id, photo_file, caption='Меню:', reply_markup=menuKeyboard)


# Обработчик для команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if bdCheckId(message.from_user.id):
        await message.answer("Привет! Я бот.", reply_markup=mainMenuKeyboard)
    else:
        bdPasteUser(message.from_user.id)
        await message.answer("Привет! Ты кто?", reply_markup=mainMenuKeyboard)


@dp.message_handler(commands=['stam'])
async def stam(message: types.Message):
    bdChangeStats(message.from_user.id, stamina=-7)
    await message.answer("-7 выносливости")


# Обработчики CallbackQuery
@dp.message_handler(Text(equals='магазин', ignore_case=True))
@dp.callback_query_handler(lambda c: c.data == 'shop')
async def shop(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id, f'Предмет ubnfhf помещён в инвентарь')



@dp.callback_query_handler(lambda c: c.data == 'stats')
async def process_callback_button2(callback: types.CallbackQuery): # Вызов меню со статистикой
    stats = bdStatistic(callback.from_user.id)
    img = stickerStats(stats)

    await callback.message.answer(f'📊Статистика📊\n'
                                  f'{img[0]}Здоровье: {stats[0]}\n'
                                  f'🎿Энергия: {stats[1]}\n'
                                  f'💰Деньги {stats[2]}\n'
                                  f'🪪Репутация: {stats[3]}\n'
                                  f'{img[1]}Скорость: {stats[4]}\n'
                                  f'{img[2]}Опыт: {stats[5]}\n')
    await callback.answer()


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
