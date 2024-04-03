from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from config import SQLALCHEMY_URL

engine = create_async_engine(SQLALCHEMY_URL, echo=True)
async_session = AsyncSession(engine)
Base = declarative_base()

class Attraction(Base):
    __tablename__ = 'attractions'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    name = Column(String)
    description = Column(String)
    photo = Column(LargeBinary)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
