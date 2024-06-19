import asyncio

from aiogram.exceptions import TelegramBadRequest
from sqlalchemy import select

from yandex import YandexFunctions
from db import async_session_maker
from db.models import YandexDiskFolder, User


async def check_updates(bot):
    while True:
        async with async_session_maker() as session:
            # Получаем все папки из базы данных
            folders = (await session.execute(select(YandexDiskFolder))).scalars().all()

            # Проверяем каждую папку
            for folder in folders:
                # Получаем преподавателя, связанного с папкой
                teacher = await session.get(User, folder.user_teacher_id)

                # Получаем дату последнего изменения папки на Яндекс.Диске
                client = YandexFunctions(token=teacher.token)
                date = await client.last_date(folder.name)

                # Если дата изменилась, обновляем её в базе и уведомляем пользователей
                if date != folder.date:
                    folder.date = date
                    await session.commit()

                    # Получаем всех слушателей, привязанных к этому преподавателю
                    users = (await session.execute(select(User).filter_by(user_teacher_id=folder.user_teacher_id))).scalars().all()

                    # Уведомляем каждого слушателя
                    for user in users:
                        try:
                            await bot.send_message(chat_id=user.id, text=f"Изменение в папке {folder.name}")
                        except TelegramBadRequest as e:
                            print(f"Не удалось отправить сообщение пользователю {user.id}: {e}")

        # Следующая проверка через час
        await asyncio.sleep(60 * 60)
