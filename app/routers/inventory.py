from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import logging
from .. import schemas, models, database
from ..schemas.inventory import InventoryUpdate

# Configure logging
logging.basicConfig(level=logging.INFO)

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Inventory])
def get_inventory(db: Session = Depends(get_db)):
    try:
        logging.info("Fetching inventory data...")
        inventory_data = db.query(models.Inventory).all()
        logging.info(f"Fetched {len(inventory_data)} inventory items.")
        return inventory_data
    except Exception as e:
        logging.error(f"Error fetching inventory data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/low-stock", response_model=List[schemas.Inventory])
def low_stock_alert(threshold: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Inventory).filter(models.Inventory.quantity < threshold).all()

@router.put("/update/{inventory_id}", response_model=schemas.Inventory)
def update_inventory(inventory_id: int, payload: InventoryUpdate, db: Session = Depends(get_db)):
    print(f"Received inventory_id: {inventory_id}")
    inventory_item = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if inventory_item:
        print(f"Found inventory item: {inventory_item.id}, Product ID: {inventory_item.product_id}")
        inventory_item.quantity = payload.quantity
        db.commit()
        db.refresh(inventory_item)
        return inventory_item
    print("Inventory item not found")
    raise HTTPException(status_code=404, detail="Inventory item not found")
