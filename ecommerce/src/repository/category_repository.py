from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model import Category


class CategoryRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,category:Category):
        self.session.add(category)
        await self.session.flush()
        await self.session.refresh(category)
        return category
    async def fetch_all(self):
        statement = select(Category)
        result = await self.session.execute(statement)
        return result.scalars().all()