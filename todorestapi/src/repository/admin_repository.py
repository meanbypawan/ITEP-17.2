from select import select

from sqlalchemy.ext.asyncio import AsyncSession

from src.model import Admin


class AdminRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,admin:Admin):
        self.session.add(admin)
        await self.session.flush()
        await self.session.refresh(admin)
        return admin

    async def fetch_by_email(self,email:str):
        statement = select(Admin).where(Admin.email == email)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()