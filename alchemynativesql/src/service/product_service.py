from src.dao.product_dao import ProductDAO
from src.model import Product


class ProductService:
    def __init__(self,session):
        self.product_dao = ProductDAO(session)

    def create_product(self,p:Product):
        return self.product_dao.create_product(p)

    def fetch_product(self):
        return self.product_dao.fetch_products()
    def fetch_expensive_product(self):
        return self.product_dao.fetch_expensive_product()