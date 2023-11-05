class Product:

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return self.quantity_in_stock > 0


eggs = Product("eggs", "food", 1)
print(eggs.is_available())
