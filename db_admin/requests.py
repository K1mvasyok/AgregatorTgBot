from sqlalchemy import select, update
from sqlalchemy.orm import joinedload, selectinload

from db_admin.models import Attraction, async_session 

attraction = Attraction(city='City', name='Name', description='Description')

async def get_faculties():
    async with async_session as session:
        result = await session.execute(select(Attraction))
        return result.scalars().all()
    
async def add_attraction(attraction):
    async with async_session as session:
        session.add(attraction)
        await session.commit()