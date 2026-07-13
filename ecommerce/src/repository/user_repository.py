from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model import User
class UserRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,user:User):
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def fetch_by_email(self,email:str):
        statement = select(User).where(User.email == email)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def fetch_all(self):
        statement = select(User)
        result = await self.session.execute(statement)
        return result.scalars().all()
    async def fetch_by_id(self,id:int):
        return await self.session.get(User,id)