from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Inventory])
def get_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()

@router.get("/low-stock", response_model=list[schemas.Inventory])
def low_stock_alert(threshold: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Inventory).filter(models.Inventory.quantity < threshold).all()

@router.put("/update/{product_id}", response_model=schemas.Inventory)
def update_inventory(product_id: int, quantity: int, db: Session = Depends(get_db)):
    inventory_item = db.query(models.Inventory).filter(models.Inventory.product_id == product_id).first()
    if inventory_item:
        inventory_item.quantity = quantity
        db.commit()
        db.refresh(inventory_item)
        return inventory_item
    return {"error": "Product not found in inventory"}
