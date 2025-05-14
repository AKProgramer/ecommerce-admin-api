from pydantic import BaseModel

class InventoryBase(BaseModel):
    product_id: int
    quantity: int

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    quantity: int

class Inventory(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True
