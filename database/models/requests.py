from sqlalchemy import select, update, delete
from sqlalchemy.sql.elements import BinaryExpression

from database import async_session_factory, User


class UserTable(object):
    @staticmethod
    async def create_by_id(id_: int) -> bool:
        try:
            async with async_session_factory() as session:
                user: User = User(id=id_)
                session.add(user)
                await session.commit()
                await session.close()
                return True
        except Exception as err:
            return False

    @staticmethod
    async def get_where(exp: BinaryExpression) -> User | None:
        try:
            async with async_session_factory() as session:
                expression = select(User).where(exp)
                query = await session.execute(expression)
                user: User = query.scalar()
                await session.close()
                return user
        except Exception as err:
            return None

    @staticmethod
    async def get_by_id(id_: int) -> User | None:
        try:
            async with async_session_factory() as session:
                user: User = await session.get(User, id_)
                await session.close()
                return user
        except Exception as err:
            return None

    @staticmethod
    async def update_by_id(id_: int, **kwargs) -> bool:
        try:
            async with async_session_factory() as session:
                expression = update(User).where(User.id == id_).values(kwargs)
                await session.execute(expression)
                await session.commit()
                await session.close()
                return True
        except Exception as err:
            return False

    @staticmethod
    async def del_where(exp: BinaryExpression) -> User | None:
        try:
            async with async_session_factory() as session:
                expression = delete(User).where(exp)
                await session.execute(expression)
                await session.commit()
                await session.close()
                return True
        except Exception as err:
            return False
