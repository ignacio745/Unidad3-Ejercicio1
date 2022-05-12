class Carrera:
    __codigo = ""
    __nombre = ""
    __titulo =""
    __duracion = ""
    __nivel = ""

    def __init__(self, codigo, nombre, titulo, duracion, nivel):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__nivel = nivel
    

    def getNombre(self):
        return self.__nombre
    
    def getDuracion(self):
        return self.__duracion
    
    def getCodigo(self):
        return self.__codigo