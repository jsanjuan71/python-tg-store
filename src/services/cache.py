
class CacheService(object): # Hereda de object
    # __ equivale a private 
    __cache = dict()

    def __new__(self): #llamado cuando se instancia un objeto
        if not hasattr(self, "instance"): #si no tiene el objeto instance
            self.instance = super(CacheService, self).__new__(self) #Genera nueva instancia de la clase CacheService
        return self.instance # Retorna la nueva o existente instancia

    def __init__(self):
        print("Soy en constructor de un singleton")


    def get(self, key): # Obtener un elemento 
        if key in self.__cache:
            return self.__cache[key]
        else: return None

    def set(self, key, value): #Asignar un nuevo valor a determinado elemento
        self.__cache[key] = value
    
    def getKeys(self): #Obtener la lista de los nombres de los elementos
        return self.__cache.keys()

    def clean(self): #Eliminar la caché
        self.__cache.clear()


