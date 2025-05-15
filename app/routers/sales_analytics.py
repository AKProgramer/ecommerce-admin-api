from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from .. import schemas, models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/by-product/{product_id}", response_model=List[schemas.Sale])
def sales_by_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(models.Sale).filter(models.Sale.product_id == product_id).all()

@router.get("/by-category/{category_id}", response_model=List[schemas.Sale])
def sales_by_category(category_id: int, db: Session = Depends(get_db)):
    return db.query(models.Sale).join(models.Product, models.Sale.product_id == models.Product.id).filter(models.Product.category_id == category_id).all()
