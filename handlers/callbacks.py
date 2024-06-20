from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from db import async_session_maker, User





async def start_callback(callback: CallbackQuery):
    await callback.answer()
    role = callback.data.split("_")[1]

    async with async_session_maker() as session:
        session: AsyncSession

        # преподаватель
        if role == "t":
            new_user = User(id=callback.from_user.id, name=callback.from_user.username)
            session.add(new_user)
            await session.commit()
            await callback.message.answer(f"Вы зарегистрировались как преподаватель")
        else:
            await callback.message.answer("Введите id вашего преподавателя:")

