from fastapi import APIRouter, HTTPException
from app.services.product_service import ProductService
from app.models.product import Product

router = APIRouter()
service = ProductService()

@router.get("/products")
def get_products():
    return service.get_all_products()

@router.get("/products/{product_id}")
def get_product(product_id: int):
    product = service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products")
def create_product(product: Product):
    return service.create_product(product)

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    return service.delete_product(product_id)

