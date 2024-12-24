from app.db import SessionLocal
from app.models.product import Product

class ProductRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self):
        return self.db.query(Product).all()

    def get_by_id(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create(self, product: Product):
        self.db.add(product)
        self.db.commit()
        return product

    def delete(self, product_id: int):
        product = self.get_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()

