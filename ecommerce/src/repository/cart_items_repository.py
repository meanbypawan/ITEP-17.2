from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model import CartItems


class CartItemsRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def save_product_in_cart(self,cart_items:CartItems):
        self.session.add(cart_items)
        await self.session.flush()
        await self.session.refresh(cart_items)
        return cart_items
    async def fetch_cart_items_by_product_id(self,product_id:int,cart_id:int):
        statement = select(CartItems).where(CartItems.product_id == product_id, CartItems.cart_id == cart_id)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()