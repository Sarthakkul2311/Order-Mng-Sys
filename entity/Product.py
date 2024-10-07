class Product:
    def __init__(self, productId, productName, description, price, quantityInStock, type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

    def __str__(self):
        return f"{self.productName} ({self.type}) - ${self.price}, Stock: {self.quantityInStock}"
    
    # Getters
    def get_product_id(self):
        return self.productId

    def get_product_name(self):
        return self.productName

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantity_in_stock(self):
        return self.quantityInStock

    def get_type(self):
        return self.type

    # Setters
    def set_product_id(self, productId):
        self.productId = productId

    def set_product_name(self, productName):
        self.productName = productName

    def set_description(self, description):
        self.description = description

    def set_price(self, price):
        self.price = price

    def set_quantity_in_stock(self, quantityInStock):
        self.quantityInStock = quantityInStock

    def set_type(self, type):
        self.type = type
