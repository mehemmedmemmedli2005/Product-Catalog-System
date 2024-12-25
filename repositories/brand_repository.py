from app.models.brand import Brand

class BrandRepository:
    def __init__(self):
        self.brands = []
        self.next_id = 1

    def add_brand(self, brand):
        brand.id = self.next_id
        self.brands.append(brand)
        self.next_id += 1
        return brand

    def get_all_brands(self):
        return self.brands

    def get_brand_by_id(self, brand_id):
        for brand in self.brands:
            if brand.id == brand_id:
                return brand
        return None
