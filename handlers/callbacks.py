from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from db import async_session_maker, User

async def start_callback(callback: CallbackQuery):
    # Отправляем подтверждение обработки коллбэк-запроса
    await callback.answer()

    # Извлекаем роль пользователя из данных коллбэк-запроса
    role = callback.data.split("_")[1]

    async with async_session_maker() as session:
        session: AsyncSession

        # Если пользователь выбрал роль "преподаватель"
        if role == "t":
            # Создаём нового пользователя в базе данных
            new_user = User(id=callback.from_user.id, name=callback.from_user.username)
            session.add(new_user)
            await session.commit()

            # Отправляем сообщение пользователю о успешной регистрации
            await callback.message.answer(f"Вы зарегистрировались как преподаватель")

        # Если пользователь выбрал другую роль
        else:
            # Отправляем запрос пользователю на ввод ID преподавателя
            await callback.message.answer("Введите ID вашего преподавателя:")
