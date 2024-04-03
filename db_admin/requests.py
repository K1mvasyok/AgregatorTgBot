from sqlalchemy import select, update
from sqlalchemy.orm import joinedload, selectinload

from db_admin.models import Attractio, async_session 

async def get_faculties():
    async with async_session as session:
        result = await session.execute(select(Attractio))
        return result.scalars().all()