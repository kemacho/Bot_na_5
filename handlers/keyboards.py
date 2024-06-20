from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

regt = InlineKeyboardButton(
    text="Преподаватель",
    callback_data="reg_t"
)

regl = InlineKeyboardButton(
    text="Ученик",
    callback_data="reg_l"
)

registerbutton = InlineKeyboardMarkup(inline_keyboard=[[regl, regt]])
