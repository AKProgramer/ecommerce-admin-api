from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, database
from ..schemas.inventory import InventoryUpdate

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Inventory])
def get_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()

@router.get("/low-stock", response_model=List[schemas.Inventory])
def low_stock_alert(threshold: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Inventory).filter(models.Inventory.quantity < threshold).all()

@router.put("/update/{product_id}", response_model=schemas.Inventory)
def update_inventory(product_id: int, payload: InventoryUpdate, db: Session = Depends(get_db)):
    inventory_item = db.query(models.Inventory).filter(models.Inventory.product_id == product_id).first()
    if inventory_item:
        inventory_item.quantity = payload.quantity
        db.commit()
        db.refresh(inventory_item)
        return inventory_item
    return {"error": "Product not found in inventory"}
