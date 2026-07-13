from fastapi import Depends

from src.dependency.repository_dependency import get_user_repository, get_category_repository, get_product_repository, \
    get_cart_repository, get_cart_items_repository
from src.repository.cart_items_repository import CartItemsRepository
from src.repository.cart_repository import CartRepository
from src.repository.category_repository import CategoryRepository
from src.repository.product_repository import ProductRepository
from src.repository.user_repository import UserRepository
from src.service.cart_service import CartService
from src.service.category_service import CategoryService
from src.service.product_service import ProductService
from src.service.user_service import UserService


def get_user_service(user_repo:UserRepository=Depends(get_user_repository)):
    return UserService(user_repo)

def get_category_service(category_repo:CategoryRepository = Depends(get_category_repository)):
    return CategoryService(category_repo)

def get_product_service(product_repo:ProductRepository=Depends(get_product_repository)):
    return ProductService(product_repo)

def get_cart_service(
        user_repo:UserRepository=Depends(get_user_repository),
        product_repo:ProductRepository=Depends(get_product_repository),
        cart_repo:CartRepository=Depends(get_cart_repository),
        cart_items_repo:CartItemsRepository=Depends(get_cart_items_repository)
):
    return CartService(user_repo,product_repo,cart_repo,cart_items_repo)