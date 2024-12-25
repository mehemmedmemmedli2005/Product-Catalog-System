from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Product Catalog API!"}

# Product Model
class Product(BaseModel):
    product_id: int = Field(..., gt=0, description="Unique identifier for the product")
    name: str = Field(..., min_length=1, max_length=100, description="Name of the product")
    price: float = Field(..., gt=0, description="Price of the product in USD")
    category: str = Field(..., min_length=1, max_length=50, description="Category of the product")

# Temporary In-Memory Database
class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def get_product(self, product_id: int):
        return self.products.get(product_id)

    def delete_product(self, product_id: int):
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")
        del self.products[product_id]

    def list_products(self):
        return list(self.products.values())

manager = ProductManager()

# API Routes
@app.post("/products", status_code=201, response_model=Product)
def create_product(product: Product):
    """
    Create a new product.
    """
    try:
        manager.add_product(product)
        return product
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products", response_model=List[Product])
def get_products():
    """
    Retrieve all products.
    """
    return manager.list_products()

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    """
    Retrieve a product by its ID.
    """
    product = manager.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found.")
    return product

@app.delete("/products/{product_id}", status_code=200)
def delete_product(product_id: int):
    """
    Delete a product by its ID.
    """
    try:
        product = manager.get_product(product_id)
        if product:
            manager.delete_product(product_id)
            return {"message": "Product deleted successfully", "product": product}
        else:
            raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found.")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
