from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class RequestStatusEnum(str, Enum):
    pending = "pending"
    accepted = "accepted"

class RequestCreate(BaseModel):
    product_id: int
    vendors_id: int
    count: int

class RequestOut(BaseModel):
    id: int
    code: int
    product_name: int
    vendors_name: int
    address: str
    customer_name: int
    count: int
    date: datetime
    status: RequestStatusEnum

    class Config:
        orm_mode = True
