from app.models.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def add_product(self, product):
        product.id = self.next_id
        self.products.append(product)
        self.next_id += 1
        return product

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def update_product(self, product_id, updated_product):
        for index, product in enumerate(self.products):
            if product.id == product_id:
                self.products[index] = updated_product
                return updated_product
        return None

    def delete_product(self, product_id):
        for index, product in enumerate(self.products):
            if product.id == product_id:
                del self.products[index]
                return True
        return False
