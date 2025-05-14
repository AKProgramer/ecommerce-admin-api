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

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd ecommerce-admin-api
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:
   - Ensure MySQL is running.
   - Run the `generate_demo_data.sql` script to create the database and populate it with demo data.

6. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

7. Access the API documentation at:
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

## Dependencies
- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- MySQL

## Testing
Run unit tests using:
```bash
pytest
```
