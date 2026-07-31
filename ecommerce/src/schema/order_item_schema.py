from typing import Optional

from pydantic import BaseModel


class OrderItemSchema(BaseModel):
    title:str
    price:float
    qty:int
    totalPrice:float
    product_image:str
    id:int
    warranty_information:Optional[str]
    description:str