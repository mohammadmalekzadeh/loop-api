from pydantic import BaseModel
from typing import Optional, List

class createProducts(BaseModel):
    name: str
    type: str
    price: int
    inventory: int

class updateProducts(BaseModel):
    is_active: bool

class filterProducts(BaseModel):
    type: Optional[str] = None
    shop_name: Optional[str] = None
    price: Optional[str] = None # from min or max
    rate: Optional[str] = None # from min or max
    is_popular: Optional[bool] = None # True or False (sort by buy_freq)

class editProducts(BaseModel):
    name: str
    type: str
    price: int
