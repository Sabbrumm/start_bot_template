from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from config import config

CREDENTIALS = f'{config.database.database_login()}:{config.database.database_password()}' \
              f'@' \
              f'{config.database.database_ip()}:{config.database.database_port()}'
DATABASE_URL = f'postgresql+asyncpg://{CREDENTIALS}/{config.database.database_name()}'

Base = declarative_base()

async_engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
async_session_factory: sessionmaker = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
