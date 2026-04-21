class Category:
    def __init__(self, category_name):
        self.category_name = category_name

    def info(self):
        return f"Category name: {self.category_name}"


category = Category("Clothing")
print(category.info())


class SubCategory(Category):
    def __init__(self, category_name, sub_category_name):
        super().__init__(category_name)
        self.sub_category_name = sub_category_name

    def info(self):
        return f"Subcategory name: {self.sub_category_name}, {super().info()}"


sub_category = SubCategory("Clothing", "Shirts")
print(sub_category.info())
