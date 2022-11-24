from ..product import Product

class ProductMapper():

    def toEntity(product):
        newProduct = Product(
            id= product.get("id"),
            title= product.get("title"),
            price= product.get("price"),
            currency= product.get("currency_id"),
            available_quantity = product.get("available_quantity"),
            thumbnail= product.get("thumbnail"),
            condition= product.get("condition")
        )
        return newProduct
    
    def serialize(product):
        return product.__dict__
    
    

