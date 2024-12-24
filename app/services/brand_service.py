from app.repositories.brand_repository import BrandRepository
from app.models.brand import Brand  # Import the Brand model

class BrandService:
    def __init__(self):
        self.repository = BrandRepository()

    def create_brand(self, name):
        brand = Brand(None, name)  # Create a new Brand instance
        return self.repository.add_brand(brand)

    def get_all_brands(self):
        return self.repository.get_all_brands()

    def get_brand(self, brand_id):
        return self.repository.get_brand_by_id(brand_id)