from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from app.database import Base
from datetime import datetime

class InventoryHistory(Base):
    __tablename__ = "inventory_history"

    id = Column(Integer, primary_key=True, index=True)
    inventory_id = Column(Integer, ForeignKey("inventory.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    change_amount = Column(Integer)
    reason = Column(String(255))
    changed_at = Column(DateTime, default=datetime.utcnow)
