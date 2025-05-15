from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from datetime import date, timedelta
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

@router.get("/weekly")
def get_weekly_revenue(db: Session = Depends(get_db)):
    today = date.today()
    week_ago = today - timedelta(days=7)
    total_revenue = db.query(models.Sale).filter(models.Sale.sale_date >= week_ago).with_entities(func.sum(models.Sale.total_price)).scalar()
    return {"start_date": week_ago.isoformat(), "end_date": today.isoformat(), "total_revenue": total_revenue or 0.0}

@router.get("/monthly")
def get_monthly_revenue(db: Session = Depends(get_db)):
    today = date.today()
    month_ago = today.replace(day=1)
    total_revenue = db.query(models.Sale).filter(models.Sale.sale_date >= month_ago).with_entities(func.sum(models.Sale.total_price)).scalar()
    return {"start_date": month_ago.isoformat(), "end_date": today.isoformat(), "total_revenue": total_revenue or 0.0}

@router.get("/annual")
def get_annual_revenue(db: Session = Depends(get_db)):
    today = date.today()
    year_ago = today.replace(month=1, day=1)
    total_revenue = db.query(models.Sale).filter(models.Sale.sale_date >= year_ago).with_entities(func.sum(models.Sale.total_price)).scalar()
    return {"start_date": year_ago.isoformat(), "end_date": today.isoformat(), "total_revenue": total_revenue or 0.0}
