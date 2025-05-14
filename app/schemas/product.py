from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(BaseModel):
    id: int

    model_config = {
        "from_attributes": True
    }
