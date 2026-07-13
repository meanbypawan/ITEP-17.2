from fastapi import UploadFile

from src.model import Product
from src.repository.product_repository import ProductRepository
from pathlib import Path
import shutil
BASE_DIR = Path(__file__).resolve().parent.parent
class ProductService:
    def __init__(self,product_repo:ProductRepository):
        self.product_repo = product_repo

    async def create(self,title:str,price:float,description:str,warranty_information:str,rating:str,product_image:UploadFile,category_id:int):
        print(f"{title} : {price} : {description} : {warranty_information} : {rating} : {product_image} : {category_id}")
        filepath = BASE_DIR.joinpath("public","images",product_image.filename)
        with open(filepath,"wb") as buffer:
            shutil.copyfileobj(product_image.file,buffer)
        await product_image.close()
        product = Product(title=title,price=price,description=description,warranty_information=warranty_information,rating=rating,category_id=category_id,product_image="/public/images/"+product_image.filename)
        return await self.product_repo.create(product)

    async def fetch_all(self):
        return await self.product_repo.fetch_all()