import os
import requests
from models.mappers.product import ProductMapper
from services.cache import CacheService

cache = CacheService()

class ProductService:

    API_URL = os.environ["ML_API_URL"]

    def __str__(self):
        print("Product service")

    def searchByKeyword(self, keyword):

        cached = cache.get(keyword) #intentar obtener desde caché
        if cached == None: # No existe en caché, invocar al API de ML
            print("Getting from ML API")
            api_response = requests.get(f"{self.API_URL}/search?q={keyword}", verify=False)
            if(api_response.status_code == 200):
                list = []
                payload = api_response.json()
                for value in payload.get("results"):
                    mapped = ProductMapper.toEntity(value)
                    list.append( ProductMapper.serialize(mapped) )
                cache.set(keyword, list) #Guardar en caché
                return list
                
            else:
                return api_response.status_code
        else: #Existe en caché
            print("Getting from cache")
            return cached
