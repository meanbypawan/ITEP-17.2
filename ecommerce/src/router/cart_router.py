from fastapi import APIRouter, Depends
from starlette import status

from src.dependency.service_dependency import get_cart_service
from src.schema.cart_schema import CartRequest
from src.service.cart_service import CartService

router = APIRouter(prefix="/cart",tags=["cart"])

@router.post("/",status_code=status.HTTP_201_CREATED)
async def add_to_cart(request:CartRequest,
                      cart_service:CartService=Depends(get_cart_service)):
    return await cart_service.add_to_cart(request)

@router.get("/{user_id}")
async def fetch_cart(user_id:int,cart_service:CartService=Depends(get_cart_service)):
   return await cart_service.fetch_cart(user_id)