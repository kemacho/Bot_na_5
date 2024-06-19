from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

engine = create_async_engine(url="sqlite+aiosqlite:///instance/sqlite.db", echo=True)

# Создаем фабрику сеансов, которая будет создавать асинхронные сеансы AsyncSession
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def async_create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
