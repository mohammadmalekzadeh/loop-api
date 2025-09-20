from pydantic import BaseModel

class vendorsOption(BaseModel):
    nation_code: str
    shop_name: str
    shop_address: str
    start_day: str
    end_day: str
    start_time: str
    end_time: str
