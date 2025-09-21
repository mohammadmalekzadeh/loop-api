from pydantic import BaseModel

class createProducts(BaseModel):
    name: str
    type: str
    price: int

class updateProducts(BaseModel):
    is_active: bool

