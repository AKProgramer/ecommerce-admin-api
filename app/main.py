from fastapi import FastAPI

from .routers import product, inventory, sales, revenue

app = FastAPI()

# Include routers
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(revenue.router, prefix="/revenue", tags=["Revenue"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce Admin API!"}
