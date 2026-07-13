from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model import Cart


class CartRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def fetch_cart_by_user_id(self,user_id:int):
        statement = select(Cart).where(Cart.user_id == user_id)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def create_cart(self,cart:Cart):
        self.session.add(cart)
        await self.session.flush()
        await self.session.refresh(cart)
        return cart