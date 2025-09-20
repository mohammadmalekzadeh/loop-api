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
