# Этап 4

# Дополнительный гайд по aiogram https://mastergroosha.github.io/aiogram-3-guide/quickstart/
# Дополнительный гайд по асинхронному бэкенду https://habr.com/ru/companies/kts/articles/598575/
# Дополнительный гайд по логированию https://habr.com/ru/companies/wunderfund/articles/683880/

# Установить библиотеки и фреймворки aiogram==3.4
# pip install aiogram
# pip install python-dotenv
# pip install sqlalchemy
# pip install aiosqlite

# Для сохранения текущих пакетов в проекте и их версий при переносе используйте файл requirements.txt
# pip freeze — внешние пакеты проекта
# pip freeze > requirements.txt — сохранить внешние пакеты в файл
# pip install -r requirements.txt —  загрузить пакеты из файла


import asyncio
import logging

from aiogram import Bot, Dispatcher

from yandex import YandexFunctions
from config import TOKEN_URL
from db import async_create_table
from functions import check_updates
from handlers import commands_for_bot
from handlers import register_message_handler

# асинхронный вызов функции - конкурентный вызов с ожиданием события для продолжения процесса выполнения

async def main():
    """Настройки перед запуском"""

    # уровень логирования
    logging.basicConfig(level=logging.INFO)

    # создание экземпляров классов Bot и Dispatcher
    dp = Dispatcher()

    bot = Bot(token="TOKEN_URL")

    # функция для вызова хендлеров из пакета handlers
    register_message_handler(dp)

    # передача списка команд боту
    await bot.set_my_commands(commands=commands_for_bot)

    # проверка обновлений в яндекс диске
    asyncio.create_task(check_updates(bot=bot))

    await dp.start_polling(bot)


# запуск бота через long_polling
if __name__ == "__main__":
    try:
        asyncio.run(async_create_table())
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logging.info("Goodbye!")
