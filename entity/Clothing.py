from entity.Product import Product

class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, "Clothing")
        self.size = size
        self.color = color

    # Getters
    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    # Setters
    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color
