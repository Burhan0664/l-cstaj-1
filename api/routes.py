from typing import List

from fastapi import APIRouter, HTTPException

from api.services import UserService
from api.models import User
from .services import ProductService
from .models import Product
from .services import OrderService
from .models import Order

case_router = APIRouter(prefix="/user")
case_service = UserService()

@case_router.get("/", response_model=List[User])
async def get_users():
    return await case_service.gets()

@case_router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = await case_service.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@case_router.post("/", response_model=User)
async def add_user(user: User):
    return await case_service.post(user)

@case_router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, data: User):
    user = await case_service.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await case_service.put(user_id, data)

@case_router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    result = await case_service.delete(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

product_router = APIRouter(prefix="/product")
product_service = ProductService()

@product_router.get("/", response_model=List[Product])
async def get_products():
    return await product_service.gets()

@product_router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = await product_service.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@product_router.post("/", response_model=Product)
async def add_product(product: Product):
    return await product_service.post(product)

@product_router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, data: Product):
    product = await product_service.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return await product_service.put(product_id, data)

@product_router.delete("/{product_id}", response_model=dict)
async def delete_product(product_id: int):
    result = await product_service.delete(product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

order_router = APIRouter(prefix="/order")
order_service = OrderService()

@order_router.get("/", response_model=List[Order])
async def get_orders():
    return await order_service.gets()

@order_router.get("/{order_id}", response_model=Order)
async def get_order(order_id: int):
    order = await order_service.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@order_router.post("/", response_model=Order)
async def add_order(order: Order):
    return await order_service.post(order)

@order_router.put("/{order_id}", response_model=Order)
async def update_order(order_id: int, data: Order):
    order = await order_service.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return await order_service.put(order_id, data)

@order_router.delete("/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    result = await order_service.delete(order_id)
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}