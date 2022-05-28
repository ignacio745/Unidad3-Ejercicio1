from Carrera import Carrera

class ManejadorCarreras:
    __carreras = None
    __actual = 0

    def __init__(self):
        self.__carreras = []
        self.__actual = 0
    

    def agregarCarrera(self, unaCarrera):
        if isinstance(unaCarrera, Carrera):
            self.__carreras.append(unaCarrera)
    

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__actual >= len(self.__carreras):
            self.__actual = 0
            raise StopIteration
        else:
            unaCarrera = self.__carreras[self.__actual]
            self.__actual += 1
            return unaCarrera
    
    def buscarCarreraPorNombre(self, nombre):
        i = 0
        while i < len(self.__carreras) and self.__carreras[i].getNombre().lower() != nombre.lower():
            i += 1
        if i == len(self.__carreras):
            i = -1
        return i
    
    
    def getCarreraPorNombre(self, nombre):
        carrera = None
        indice = self.buscarCarreraPorNombre(nombre)
        if indice != -1:
            carrera = self.__carreras[indice]
        return carrera