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
    
    def __str__(self):
        return f"{self.id}: {self.title}"