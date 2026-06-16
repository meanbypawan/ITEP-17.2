from src.dao.product_dao import ProductDAO
from src.model import Product


class ProductService:
    def __init__(self,session):
        self.product_dao = ProductDAO(session)

    def create_product(self,p:Product):
        return self.product_dao.create_product(p)

    def fetch_products(self):
        return self.product_dao.fetch_products()

    def delete_product(self,pid:int):
        return self.product_dao.delete_product(pid)

    def update_product(self,pid:int,p:Product):
       return self.product_dao.update_product(pid,p)






