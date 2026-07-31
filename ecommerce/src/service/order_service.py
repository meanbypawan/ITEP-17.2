from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Order, OrderItems
from src.repository.order_repository import OrderRepository
from src.repository.user_repository import UserRepository
from src.schema.order_schema import OrderRequest


class OrderService:
    def __init__(self,order_repo:OrderRepository,user_repo:UserRepository):
        self.order_repo = order_repo
        self.user_repo = user_repo

    async def save(self,request:OrderRequest):
        user_id = request.user_id
        user = await self.user_repo.fetch_by_id(user_id)
        if not user:
            raise ResourceNotFoundException(f"User with id {user_id} not found")
        order = Order(user_id=request.user_id,
                      name=request.name,
                      email=request.email,
                      contact=request.contact,
                      address=request.address,
                      totalBillAmount=request.totalBillAmount,
                      )
        item_list = request.order_items
        order_items = []
        for item in item_list:
            oi = OrderItems(title=item.title,
                            price=item.price,
                            description=item.description,
                            qty=item.qty,
                            warranty_information=item.warranty_information,
                            totalPrice=item.totalPrice,
                            product_id=item.id,
                            product_image=item.product_image
                            )
            order_items.append(oi)
        order.order_items = order_items
        return await self.order_repo.save(order)