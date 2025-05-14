from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(BaseModel):
    id: int

    model_config = {
        "from_attributes": True
    }
