import json
import os
from queue import Full
from typing import List

from .models import User
from .models import Product
from .models import Order

class UserService:
    """
    Kullanıcılar için CRUD Servisi
    """

    def __init__(self):
        pass

    async def gets(self) -> List[User]:
        try:
           with open('data.json', 'r') as file:
                users_data = json.load(file)
        except json.decoder.JSONDecodeError as e:
            print("JSON decoding error:", e)
            return []  # Return an empty list if JSON decoding fails

        users = [User(**user) for user in users_data]
        return users

    async def get(self, user_id: int) -> User:
        users = await self.gets()
        for user in users:
           if user.id == user_id:
               return user
        return {"error":"This user doest not exist"}

    async def post(self, user: User) -> User:
      with open("data.json", "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
      for existing_user in data:
        if user.id == existing_user['id']:
            return {"error": "İd already exists"}

      data.append(user.dict())
       
      with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
      return user

    async def put(self, user_id: int, data: User) -> User:
        users = await self.gets()
        for user in users:
            if user.id == user_id:
                user.username = data.username
                user.email = data.email
                user.full_name = data.full_name
                break
        with open('data.json', 'w') as file:
            json.dump([u.dict() for u in users], file, indent=4)
        return data

    async def delete(self, user_id: int) -> int:
        users = await self.gets()
        users = [user for user in users if user.id != user_id]
        
        with open('data.json', 'w') as file:
             json.dump([u.dict() for u in users], file, indent=4)
        return user_id
    
class OrderService:


    def __init__(self):
        pass

    async def gets(self) -> List[Order]:
        try:
           with open('data.json', 'r') as file:
                orders_data = json.load(file)
        except json.decoder.JSONDecodeError as e:
            print("JSON decoding error:", e)
            return []  # Return an empty list if JSON decoding fails

        orders = [Order(**order) for order in orders_data]
        return orders

    async def get(self, order_id: int) -> Order:
        orders = await self.gets()
        for order in orders:
           if order.id == order_id:
               return order
        return {"error":"This order does not exist"}

    async def post(self, order: Order) -> Order:
        with open("data.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

        for existing_user in data:
         if order.id == existing_user['id']:
            return {"error": "İd already exists"}
         
        data.append(order.dict())
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return order

    async def put(self, order_id: int, data: Order) -> Order:
        orders = await self.gets()
        for order in orders:
            if order.id == order_id:
                order.customer_id = data.customer_id
                order.products = data.products
                order.total_price = data.total_price
                order.status = data.status
                break
        with open('data.json', 'w') as file:
            json.dump([o.dict() for o in orders], file, indent=4)
        return data

    async def delete(self, order_id: int) -> int:
        orders = await self.gets()
        orders = [order for order in orders if order.id != order_id]
        
        with open('data.json', 'w') as file:
             json.dump([o.dict() for o in orders], file, indent=4)
        return order_id
    
class ProductService:


    def __init__(self):
        pass

    async def gets(self) -> List[Product]:
        try:
           with open('data.json', 'r') as file:
                products_data = json.load(file)
        except json.decoder.JSONDecodeError as e:
            print("JSON decoding error:", e)
            return []  # Return an empty list if JSON decoding fails

        products = [Product(**product) for product in products_data]
        return products

    async def get(self, product_id: int) -> Product:
        products = await self.gets()
        for product in products:
           if product.id == product_id:
               return product
        return {"error":"This product doest not exist"}

    async def post(self, product: Product) -> Product:
        with open("data.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
        for existing_user in data:
         if product.id == existing_user['id']:
            return {"error": "İd already exists"}
        
        data.append(product.dict())
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return product

    async def put(self, product_id: int, data: Product) -> Product:
        products = await self.gets()
        for product in products:
            if product.id == product_id:
                product.name = data.name
                product.description = data.description
                product.price = data.price
                product.in_stock = data.in_stock
                break
        with open('data.json', 'w') as file:
            json.dump([p.dict() for p in products], file, indent=4)
        return data

    async def delete(self, product_id: int) -> int:
        products = await self.gets()
        products = [product for product in products if product.id != product_id]
        
        with open('data.json', 'w') as file:
             json.dump([p.dict() for p in products], file, indent=4)
        return product_id