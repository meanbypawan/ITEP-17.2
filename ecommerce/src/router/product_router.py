from decimal import Decimal
from typing import Optional

from fastapi import APIRouter, Form, UploadFile, File, Depends
from starlette import status

from src.dependency.service_dependency import get_product_service
from src.service.product_service import ProductService

router = APIRouter(prefix="/product", tags=["product"])

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_product(title:str=Form(...),
                         price:Decimal=Form(...),
                         description:Optional[str]=Form(None),
                         warranty_information:Optional[str]=Form(None),
                         rating:Optional[str]=Form(None),
                         product_image:UploadFile=File(...),
                         category_id:int = Form(...),
                         product_service:ProductService=Depends(get_product_service)):

    return await product_service.create(title=title,price=price,description=description,warranty_information=warranty_information,rating=rating,product_image=product_image,category_id=category_id)

@router.get("/",status_code=status.HTTP_200_OK)
async def fetch_all(product_service:ProductService=Depends(get_product_service)):
    return await product_service.fetch_all()
