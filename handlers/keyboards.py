from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

continue_button = InlineKeyboardButton(
    text="Далее",
    callback_data="continue_button_pressed",
)

keyboard_continue = InlineKeyboardMarkup(inline_keyboard=[[continue_button]])

