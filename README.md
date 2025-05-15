# E-commerce Admin API

This project is a back-end API for an e-commerce admin dashboard, built using Python and FastAPI. It provides insights into sales, revenue, and inventory status, and allows for new product registration.

## Features

### Sales Status
- Retrieve, filter, and analyze sales data.
- Analyze revenue on a daily, weekly, monthly, and annual basis.
- Compare revenue across different periods and categories.
- Provide sales data by date range, product, and category.

### Inventory Management
- View current inventory status, including low stock alerts.
- Update inventory levels and track changes over time.
- **Track inventory change history (audit trail).**

### Sales Analytics
- Retrieve sales data by product and by category.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/AKProgramer/ecommerce-admin-api.git
   ```

2. Add your MySQL database credentials in the `app/database.py` file:
   ```
   DB_USERNAME = "root"
   DB_PASSWORD = "1234"
   DB_HOST = "localhost"
   DB_NAME = "ecommerce_db"
   ```

3. Populate the database with demo data:
   - Ensure MySQL is running.
   - Run the `script/generate_demo_data.sql` script to create the database and populate it with demo data.

4. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Database Schema

### Tables

#### Categories
- `id`: Primary key.
- `name`: Name of the category.

#### Products
- `id`: Primary key.
- `name`: Name of the product.
- `description`: Description of the product.
- `price`: Price of the product.
- `category_id`: Foreign key referencing `Categories`.

#### Inventory
- `id`: Primary key.
- `product_id`: Foreign key referencing `Products`.
- `quantity`: Quantity in stock.

#### Sales
- `id`: Primary key.
- `product_id`: Foreign key referencing `Products`.
- `quantity`: Quantity sold.
- `total_price`: Total price of the sale.
- `sale_date`: Date and time of the sale.

## Endpoints

### Sales
- `GET /sales`: Retrieve all sales.
- `GET /sales/filter`: Filter sales by date range.
- `GET /sales/compare`: Compare revenue across two periods.

### Inventory
- `GET /inventory`: Retrieve inventory status.
- `GET /inventory/low-stock`: Get low stock alerts.
- `PUT /inventory/update/{product_id}`: Update inventory levels.

### Inventory History
- `GET /inventory-history/`: Retrieve all inventory change history records.
- `GET /inventory-history/by-inventory/{inventory_id}`: Get history for a specific inventory item.
- `GET /inventory-history/by-product/{product_id}`: Get history for a specific product.

### Sales Analytics
- `GET /sales-analytics/by-product/{product_id}`: Get all sales for a specific product.
- `GET /sales-analytics/by-category/{category_id}`: Get all sales for a specific category.

## Dependencies
- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- MySQL

## Testing
Run unit tests using:
```bash
pytest tests/test_routes.py 
```

## Missing Features / Improvements

- Tracking inventory changes over time (history/audit) is not implemented.
- Endpoints for sales data by product and category are not explicitly present.
- Revenue analysis for weekly, monthly, and annual basis is not implemented (only daily).
- No explicit indexing in the SQL script, but primary keys are present.
