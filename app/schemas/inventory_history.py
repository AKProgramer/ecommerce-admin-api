from pydantic import BaseModel
from datetime import datetime

class InventoryHistoryBase(BaseModel):
    inventory_id: int
    product_id: int
    change_amount: int
    reason: str
    changed_at: datetime

class InventoryHistoryCreate(InventoryHistoryBase):
    pass

class InventoryHistory(InventoryHistoryBase):
    id: int

    model_config = {
        "from_attributes": True
    }
