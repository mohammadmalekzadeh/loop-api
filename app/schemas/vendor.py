from pydantic import BaseModel
from typing import Optional

class vendorsOption(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    nation_code: Optional[str]
    shop_name: Optional[str]
    shop_address: Optional[str]
    start_day: Optional[str]
    end_day: Optional[str]
    start_time: Optional[str]
    end_time: Optional[str]

class vendorsFilter(BaseModel):
    rate: Optional[str] = None # from min or max
    is_work: Optional[bool] = None # sort by products length
    newest: Optional[bool] = None
