import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test Sales Routes
def test_get_sales():
    response = client.get("/sales")
    assert response.status_code == 200

def test_filter_sales():
    response = client.get("/sales/filter?start_date=2025-05-01&end_date=2025-05-05")
    assert response.status_code == 200

def test_compare_revenue():
    response = client.get("/sales/compare?period1_start=2025-05-01&period1_end=2025-05-03&period2_start=2025-05-04&period2_end=2025-05-05")
    assert response.status_code == 200

# Test Inventory Routes
def test_get_inventory():
    response = client.get("/inventory")
    assert response.status_code == 200

def test_low_stock_alert():
    response = client.get("/inventory/low-stock?threshold=10")
    assert response.status_code == 200

def test_update_inventory():
    response = client.put("/inventory/update/1", json={"quantity": 20})
    assert response.status_code == 200
