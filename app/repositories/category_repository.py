from app.models.category import Category

class CategoryRepository:
    def __init__(self):
        self.categories = []
        self.next_id = 1

    def add_category(self, category):
        category.id = self.next_id
        self.categories.append(category)
        self.next_id += 1
        return category

    def get_all_categories(self):
        return self.categories

    def get_category_by_id(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category
        return None