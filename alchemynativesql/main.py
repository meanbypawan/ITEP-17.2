from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.exception.resouce_not_found_exception import ResourceNotFoundException
from src.model import Product
from src.service.product_service import ProductService


def create_product():
    try:
        with SessionLocal.begin() as session:
            title = input("Enter product title: ")
            price = float(input("Enter product price: "))
            brand = input("Enter product brand: ")
            category = input("Enter product category: ")
            dp = float(input("Enter discount percentage: "))
            # creating model object
            p = Product(title = title,price=price,brand = brand,discount_percentage = dp,category_name = category)
            # creating service and passing session
            product_service = ProductService(session)

            #calling service method and passing model object
            result = product_service.create_product(p)
            if result.rowcount == 0:
                print("Something wrong")
            else:
                print("Product created successfully")
    except SQLAlchemyError as e:
        print("Something went wrong")
        print(e)
def fetch_products():
    try:
        with SessionLocal() as session:
            product_service = ProductService(session)
            result = product_service.fetch_product()
            print(result)
    except SQLAlchemyError as e:
        print(e)
def fetch_expensive_product():
    with SessionLocal() as session:
        result =  ProductService(session).fetch_expensive_product()
        for product in result:
            print(product)

while True:
    print("1 for creating product")
    print("2 for fetching all products")
    print("3 for expensive product")
    print("0 for exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_product()
    elif choice == 0:
        break
    elif choice == 2:
        fetch_products()
    elif choice == 3:
        fetch_expensive_product()
