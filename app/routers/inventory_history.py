from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.InventoryHistory])
def get_inventory_history(db: Session = Depends(get_db)):
    return db.query(models.InventoryHistory).all()

@router.get("/by-inventory/{inventory_id}", response_model=List[schemas.InventoryHistory])
def get_history_by_inventory(inventory_id: int, db: Session = Depends(get_db)):
    return db.query(models.InventoryHistory).filter(models.InventoryHistory.inventory_id == inventory_id).all()

@router.get("/by-product/{product_id}", response_model=List[schemas.InventoryHistory])
def get_history_by_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(models.InventoryHistory).filter(models.InventoryHistory.product_id == product_id).all()
