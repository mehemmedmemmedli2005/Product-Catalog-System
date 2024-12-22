from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List

app = FastAPI()

# Model
class Product(BaseModel):
    product_id: int
    name: str
    price: float
    category: str

# Database (müvəqqəti yaddaş)
class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        if product.product_id in self.products:
            raise ValueError("Product ID already exists.")
        self.products[product.product_id] = product

    def get_product(self, product_id: int):
        return self.products.get(product_id)

    def delete_product(self, product_id: int):
        if product_id not in self.products:
            raise ValueError("Product not found.")
        del self.products[product_id]

    def list_products(self):
        return list(self.products.values())

manager = ProductManager()

# Routes
@app.post("/products", status_code=201)
def create_product(product: Product):
    try:
        manager.add_product(product)
        return {"message": "Product added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products", response_model=List[Product])
def get_products():
    return manager.list_products()

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = manager.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.delete("/products/{product_id}", status_code=200)
def delete_product(product_id: int):
    try:
        manager.delete_product(product_id)
        return {"message": "Product deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
