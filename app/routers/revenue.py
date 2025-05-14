from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from datetime import date
from .. import database, models

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/daily")
def get_daily_revenue(db: Session = Depends(get_db)):
    # Get today's date
    today = date.today()

    # Query the Sales table to calculate total revenue for today
    total_revenue = db.query(models.Sale).filter(models.Sale.sale_date == today).with_entities(func.sum(models.Sale.total_price)).scalar()

    # Return the total revenue
    return {"date": today.isoformat(), "total_revenue": total_revenue or 0.0}
