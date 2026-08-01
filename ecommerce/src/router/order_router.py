from fastapi import APIRouter, Depends
from starlette import status

from src.dependency.service_dependency import get_order_service, authenticate
from src.schema.order_schema import OrderRequest
from src.service.order_service import OrderService

router = APIRouter(prefix="/orders",tags=["orders"])

@router.post("/",status_code=status.HTTP_201_CREATED)
async def save_order(request:OrderRequest,order_service:OrderService=Depends(get_order_service),payload=Depends(authenticate)):
   saved_order =  await order_service.save(request)
   return saved_order

