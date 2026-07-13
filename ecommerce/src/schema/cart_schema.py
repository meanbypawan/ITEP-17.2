from pydantic import BaseModel


class CartRequest(BaseModel):
    user_id:int
    product_id:int