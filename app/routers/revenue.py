from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/daily")
def get_daily_revenue(db: Session = Depends(get_db)):
    # Placeholder for daily revenue logic
    return {"message": "Daily revenue endpoint"}
