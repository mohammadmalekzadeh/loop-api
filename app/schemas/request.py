from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class RequestStatusEnum(str, Enum):
    pending = "pending"
    accepted = "accepted"

class RequestCreate(BaseModel):
    product_id: int
    count: int

class RequestOut(BaseModel):
    id: int
    code: int
    product_name: str
    shop_name: str
    address: str
    customer_name: str
    count: int
    date: datetime
    jalali_date: str
    status: RequestStatusEnum
    price: int

    class Config:
        orm_mode = True

class filterRequest(BaseModel):
    status: Optional[str] = None # accepeted or pending
    date: Optional[str] = None # old or new
    code: Optional[int] = None
