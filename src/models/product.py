class Product:
    id = None
    title = None
    price = None
    currency = None
    available_quantity = None
    thumbnail_url = None
    condition = None


    def __init__(self, id, title, price, currency, available_quantity, thumbnail, condition):
        self.id = id
        self.title = title
        self.price = price
        self.currency = currency
        self.stock = available_quantity
        self.thumbnail = thumbnail
        self.condition = condition

    def retrieveTax(self):
        return self.price * 0.16

    
    def setPrecio(self, precio):
        if precio < 0:
            return None

    
    
    def __str__(self):
        return f"Soy {self.title} con id: {self.id}."

  
"""
celular = Product(1, "Samsung Galaxy", 2000, "MXN", 10, "url", "nuevo")


laptop = Product(2, "macbook pro", 15000, "MXN", 5, "url", "nuevo")
laptop.retrieveTax()
iva = celular.retrieveTax()

celular.price = 20

celular.setPrecio(20)

print(celular)

"""