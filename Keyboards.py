from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Инлай-клавы
menuKeyboard = InlineKeyboardMarkup()  #

buttonShop = InlineKeyboardButton("🛍Магазин🛍", callback_data="shop")
buttonLocations = InlineKeyboardButton("✈️Локации✈️", callback_data="locations")
buttonStats = InlineKeyboardButton("📊Статистика📊", callback_data="stats")

menuKeyboard.add(buttonShop, buttonLocations, buttonStats)
# ------------------------------------------------------


mainMenuKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)  #

buttonMenu = KeyboardButton("Меню")
button2 = KeyboardButton("✈️Локации✈️")
button3 = KeyboardButton("📊Статистика📊")

mainMenuKeyboard.add(buttonMenu)
# ------------------------------------------------------

