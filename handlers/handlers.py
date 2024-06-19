__all__ = [
    "register_message_handler",
]


import logging
from aiogram import Router, F
from aiogram import types
from aiogram.filters.command import Command
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from db import async_session_maker, User
from .keyboards import keyboard_continue
from .callbacks import callback_continue


# настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# help_command
help_str = """
Вас приветствует бот <b><i>БОТ №5</i></b>\n
💬 Вы можете вывести справочную информацию, отправив команду <b>/help</b>\n
💬 Информацию о пользователе можно вывести с помощью команды <b>/status</b>\n
💬 Для регистрации нового профиля используйте команду <b>/register</b>
"""

# List of commands for the bot
commands_for_bot = [
    BotCommand(command="/start", description="Start the bot"),
    BotCommand(command="/help", description="Get help information"),
    BotCommand(command="/info", description="Get information about the bot"),
    BotCommand(command="/fetch_data", description="Fetch data from database"),
    BotCommand(command="/add_data", description="Add data to the database"),
    BotCommand(command="/delete_data", description="Delete data from the database"),
    BotCommand(command="/update_data", description="Update data in the database"),
    BotCommand(command="/list_data", description="List all data from the database"),
]


async def help_command(message: types.Message):
    """справочная команда, регистрация пользователя"""

    async with async_session_maker() as session:
        session: AsyncSession
        query = select(User).where(User.user_id == message.from_user.id)
        user_exit = await session.execute(query)

        if user_exit.scalars().all():
            await message.reply(text=help_str, parse_mode="HTML")
            logging.info(f"user {message.from_user.id} asks for help")

        else:
            new_user = {
                "user_id": message.from_user.id,
                "username": message.from_user.username
            }
            stmt = insert(User).values(**new_user)
            await session.execute(stmt)
            await session.commit()
            await message.reply(help_str)
            logging.info(f"register new user: {message.from_user.id}")


async def status_command(message: types.Message):
    """Информация о пользователе"""

    async with async_session_maker() as session:
        session: AsyncSession
        query = select(User).where(User.user_id == message.from_user.id)
        result = await session.execute(query)
        user = result.scalar()
        await message.reply(text=f"<b>User ID</b>: <i>{user.user_id}</i>\n"
                                 f"<b>User name</b>: <i>{user.username}</i>",
                                 parse_mode="HTML")
        logging.info(f"user {message.from_user.id} is asking for status")

    await message.reply("Хотите ли вы продолжить?", reply_markup=keyboard_continue)


async def start_command(message: types.Message):
    await message.reply("Hello! I am your bot. How can I help you today?")

async def help_command(message: types.Message):
    await message.reply("This bot can handle the following commands:\n" +
                        "\n".join([f"/{cmd.command} - {cmd.description}" for cmd in commands_for_bot]))

async def info_command(message: types.Message):
    await message.reply("This bot is created to demonstrate aiogram capabilities.")

async def fetch_data_command(message: types.Message):
    await message.reply("Fetching data from the database...")

async def add_data_command(message: types.Message):
    # Example: /add_data some_data
    data = message.get_args()
    if data:
        await add_data(data)
        await message.reply("Data added successfully.")
    else:
        await message.reply("Please provide data to add. Example: /add_data some_data")

async def delete_data_command(message: types.Message):
    # Example: /delete_data 1
    data_id = message.get_args()
    if data_id.isdigit():
        await delete_data(int(data_id))
        await message.reply("Data deleted successfully.")
    else:
        await message.reply("Please provide a valid data ID to delete. Example: /delete_data 1")

async def update_data_command(message: types.Message):
    # Example: /update_data 1 new_data
    args = message.get_args().split(maxsplit=1)
    if len(args) == 2 and args[0].isdigit():
        await update_data(int(args[0]), args[1])
        await message.reply("Data updated successfully.")
    else:
        await message.reply("Please provide a valid data ID and new data. Example: /update_data 1 new_data")

async def list_data_command(message: types.Message):
    data = await list_data()
    await message.reply(f"Data in the database:\n{data}")


def register_message_handler(router: Router):
    """Маршрутизация"""
    router.message.register(start_command, commands=["start"])
    router.message.register(help_command, commands=["help"])
    router.message.register(info_command, commands=["info"])
    router.message.register(fetch_data_command, commands=["fetch_data"])
    router.message.register(add_data_command, commands=["add_data"])
    router.message.register(delete_data_command, commands=["delete_data"])
    router.message.register(update_data_command, commands=["update_data"])
    router.message.register(list_data_command, commands=["list_data"])
    router.message.register(help_command, Command(commands=["start", "help"]))
    router.message.register(status_command, Command(commands=["status"]))
    router.callback_query.register(callback_continue, F.data.startswith("continue_"))
