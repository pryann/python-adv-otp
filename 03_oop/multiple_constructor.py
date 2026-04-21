# class Category:
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.name = args[0]
#         elif len(args) == 2:
#             self.name = args[0]
#             self.description = args[1]


class Category:
    def __init__(self, name, description=""):
        self.name = name
        self.descripton = description

    @classmethod
    def from_string(cls, s):
        parts = s.split("|")
        return cls(*parts)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)


if __name__ == "__main__":
    c1 = Category("Clothing")
    print(c1.name)
    c2 = Category("Clothing", "All king of clothes")
    print(c2.name, c2.descripton)
    c3 = Category.from_string("Clothing|All king of clothes")
    print(c3.name, c3.descripton)
    c4 = Category.from_dict({"name": "Cloathing", "description": "All king of clothes"})
    print(c4.name, c4.descripton)
