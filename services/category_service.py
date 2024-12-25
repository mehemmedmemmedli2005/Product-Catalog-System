from app.repositories.category_repository import CategoryRepository
from app.models.category import Category  # Import the Category model

class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()

    def create_category(self, name):
        category = Category(None, name)  # Create a new Category instance
        return self.repository.add_category(category)

    def get_all_categories(self):
        return self.repository.get_all_categories()

    def get_category(self, category_id):
        return self.repository.get_category_by_id(category_id)
