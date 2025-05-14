from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(BaseModel):
    id: int

    class Config:
        from_attributes = True
