from pydantic import BaseModel
from typing import Optional, List

class createProducts(BaseModel):
    name: str
    type: str
    price: int
    inventory: int

class updateProducts(BaseModel):
    name: str
    type: str
    price: int
    inventory: int

class filterProducts(BaseModel):
    type: Optional[str] = None
    shop_name: Optional[str] = None
    price: Optional[str] = None # from min or max
    rate: Optional[str] = None # from min or max
    is_popular: Optional[bool] = None # True or False (sort by buy_freq)
    newest: Optional[bool] = None # True or False (sort by id for new or old)

class editProducts(BaseModel):
    name: str
    type: str
    price: int
