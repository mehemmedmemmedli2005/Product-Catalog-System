from app.repositories.product_repository import ProductRepository
from app.models.product import Product  # Import the Product model

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def create_product(self, name, description, price, category_id, brand_id):
        product = Product(None, name, description, price, category_id, brand_id)  # Create a new Product instance
        return self.repository.add_product(product)

    def get_all_products(self):
        return self.repository.get_all_products()

    def get_product(self, product_id):
        return self.repository.get_product_by_id(product_id)

    def update_product(self, product_id, updated_product):
        return self.repository.update_product(product_id, updated_product)

    def delete_product(self, product_id):
        return self.repository.delete_product(product_id)
