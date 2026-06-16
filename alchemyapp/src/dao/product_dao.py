from sqlalchemy import select

from src.exception.resouce_not_found_exception import ResourceNotFoundException
from src.model.product import Product
class ProductDAO:
    def __init__(self,session):
        self.session = session

    def update_product(self,id:int, p:Product):
        # sqlalchemy track the object
        # db_product : id : 100001
        db_product = self.session.get(Product,id)
        if not db_product:
            raise ResourceNotFoundException("Product not found")
        db_product.title = p.title
        db_product.price = p.price
        db_product.category_name = p.category_name
        db_product.brand = p.brand
        return db_product

    def delete_product(self,pid:int):
        db_product = self.session.get(Product,pid)
        if not db_product:
           raise ResourceNotFoundException("Product not found")
        self.session.delete(db_product) # alway return None
        return db_product

    def create_product(self,p:Product):
        self.session.add(p) # insert operation is pending
        self.session.flush() # it will execute pending operation
        return p

    def fetch_products(self):
        statement = select(Product)
        # [<Product-object1>,<Product-object2>,..]
        return self.session.execute(statement).scalars().all()

