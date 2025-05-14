import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.database import SessionLocal
from app.models import Product, Inventory, Sale

client = TestClient(app)

# Helper function to create test data
def setup_test_data():
    db: Session = SessionLocal()
    try:
        # Create a test product
        test_product = Product(name="Test Product", description="A test product", price=10.0, category_id=1)
        db.add(test_product)
        db.commit()
        db.refresh(test_product)

        # Create a test inventory item
        test_inventory = Inventory(product_id=test_product.id, quantity=50)
        db.add(test_inventory)
        db.commit()
        db.refresh(test_inventory)

        # Debug logs
        print(f"Test Product ID: {test_product.id}")
        print(f"Test Inventory ID: {test_inventory.id}, Product ID: {test_inventory.product_id}")
    finally:
        db.close()

# Helper function to clean up test data
def teardown_test_data():
    db: Session = SessionLocal()
    try:
        # Fetch the test product by name
        test_product = db.query(Product).filter(Product.name == "Test Product").first()
        if test_product:
            # Delete related inventory and sales entries
            db.query(Inventory).filter(Inventory.product_id == test_product.id).delete()
            db.query(Sale).filter(Sale.product_id == test_product.id).delete()
            # Delete the test product
            db.query(Product).filter(Product.id == test_product.id).delete()
        db.commit()
    finally:
        db.close()

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Setup test data
    setup_test_data()
    yield
    # Teardown test data
    teardown_test_data()

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
    assert isinstance(response.json(), list)
    if response.json():
        assert "id" in response.json()[0]
        assert "product_id" in response.json()[0]
        assert "quantity" in response.json()[0]

def test_low_stock_alert():
    response = client.get("/inventory/low-stock?threshold=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for item in response.json():
        assert item["quantity"] < 10

def test_update_inventory():
    db: Session = SessionLocal()
    try:
        # Setup test data specific to this test
        test_product = Product(name="Update Test Product", description="A test product for update", price=15.0, category_id=1)
        db.add(test_product)
        db.commit()
        db.refresh(test_product)

        test_inventory = Inventory(product_id=test_product.id, quantity=30)
        db.add(test_inventory)
        db.commit()
        db.refresh(test_inventory)

        # Debug logs
        print(f"Test Product ID: {test_product.id}")
        print(f"Test Inventory ID: {test_inventory.id}, Product ID: {test_inventory.product_id}")

        # Use the inventory item's ID for the update
        response = client.put(f"/inventory/update/{test_inventory.id}", json={"quantity": 20})
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.json()}")

        assert response.status_code == 200
        updated_item = response.json()
        assert updated_item["id"] == test_inventory.id
        assert updated_item["quantity"] == 20

        # Teardown test data specific to this test
        db.query(Inventory).filter(Inventory.id == test_inventory.id).delete()
        db.query(Product).filter(Product.id == test_product.id).delete()
        db.commit()
    finally:
        db.close()
