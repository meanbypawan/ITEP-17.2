from os import stat_result

from pydantic import BaseModel,EmailStr

from src.schema.order_item_schema import OrderItemSchema


class OrderRequest(BaseModel):
    user_id:int
    name:str
    email:EmailStr
    address:str
    contact:str
    totalBillAmount:float
    order_items:list[OrderItemSchema]