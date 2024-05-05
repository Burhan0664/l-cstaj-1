import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None


class Product(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None

    
class Order(BaseModel):
    id: int
    customer_id: Optional[int] = None
    products: Optional[List[Product]] = None
    total_price: Optional[float] = None
    status: Optional[str] = None