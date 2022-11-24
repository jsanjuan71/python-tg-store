import os
import requests
from models.mappers.product import ProductMapper
from tools.serializable import modelToJson

class ProductService:

    API_URL = os.environ["ML_API_URL"]

    def __str__(self):
        print("Product service")

    def searchByKeyword(self, keyword):
        api_response = requests.get(f"{self.API_URL}/search?q={keyword}")
        if(api_response.status_code == 200):
            list = []
            payload = api_response.json()
            for value in payload.get("results"):
                mapped = ProductMapper.toEntity(value)
                list.append( ProductMapper.serialize(mapped) )
            return list
        else:
            return api_response.status_code
