from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import schemas, models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Sale])
def get_sales(db: Session = Depends(get_db)):
    return db.query(models.Sale).all()

@router.get("/filter", response_model=list[schemas.Sale])
def filter_sales(start_date: str, end_date: str, db: Session = Depends(get_db)):
    return db.query(models.Sale).filter(models.Sale.sale_date.between(start_date, end_date)).all()

@router.get("/compare", response_model=dict)
def compare_revenue(period1_start: str, period1_end: str, period2_start: str, period2_end: str, db: Session = Depends(get_db)):
    period1_revenue = db.query(func.sum(models.Sale.total_price)).filter(models.Sale.sale_date.between(period1_start, period1_end)).scalar()
    period2_revenue = db.query(func.sum(models.Sale.total_price)).filter(models.Sale.sale_date.between(period2_start, period2_end)).scalar()
    return {"period1_revenue": period1_revenue, "period2_revenue": period2_revenue}
