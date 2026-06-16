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
            p = product_service.create_product(p)
            session.refresh(p)
            print("Product created successfully")
            print(f"Product : - {p}")
    except SQLAlchemyError as e:
        print("Something went wrong")
        print(e)

def fetch_products():
    try:
        with SessionLocal() as session:
            product_service = ProductService(session)
            product_list = product_service.fetch_products()
            for product in product_list:
                print(product)

    except SQLAlchemyError as e:
        print(e)

def delete_product():
    try:
        with SessionLocal.begin() as session:
            product_service = ProductService(session)
            id = int(input("Enter product id: "))
            p = product_service.delete_product(id)
            print("Product deleted successfully")
            print(p)
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

def update_product():
    try:
        with SessionLocal.begin() as session:
            product_service = ProductService(session)
            title = input("Enter product title: ")
            price = float(input("Enter product price: "))
            brand = input("Enter product brand: ")
            category = input("Enter product category: ")
            id = int(input("Enter product id: "))
            p = Product(title = title,price=price,brand=brand,category_name = category)
            updated_product = product_service.update_product(id,p)
            print("Product updated successfully")
            print(updated_product)
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

while True:
    print("1 for creating product")
    print("2 for fetching products")
    print("3 for delete product")
    print("4 for update product")
    print("0 for exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_product()
    elif choice == 0:
        break
    elif choice == 2:
        fetch_products()
    elif choice == 3:
       delete_product()
    elif choice == 4:
        update_product()