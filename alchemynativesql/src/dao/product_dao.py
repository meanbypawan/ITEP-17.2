from sqlalchemy import select, and_, func

from src.exception.resouce_not_found_exception import ResourceNotFoundException
from sqlalchemy import text
from src.model.product import Product
class ProductDAO:
    def __init__(self,session):
        self.session = session
    def fetch_expensive_product(self):
        statement = select(Product).from_statement(text('''
          select * from product where price in(
            select max(price) from product group by category_name)
        '''))
        return self.session.execute(statement).scalars().all()

    def fetch_products(self):
      statement = select(Product).from_statement(text("select * from product"))
      #self.session.execute(statement,{"category_name" : "Mobile"})
      return self.session.execute(statement).scalars().all()

    def create_product(self,p:Product):
        statement = text('''insert into product(title,price,brand,discount_percentage,category_name)
         values(:title,:price,:brand,:discount_percentage,:category_name)''')
        result = self.session.execute(statement,{
            "title":p.title,
            "price":p.price,
            "brand":p.brand,
            "discount_percentage":p.discount_percentage,
            "category_name":p.category_name
        })
        return result
