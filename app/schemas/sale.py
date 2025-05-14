from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    product_id: int
    quantity: int
    total_price: float
    sale_date: datetime

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int

    model_config = {
        "from_attributes": True
    }
