from Carrera import Carrera
from ManejadorCarreras import ManejadorCarreras

class Facultad:
    __codigo = None
    __nombre = None
    __direccion = None
    __localidad = None
    __telefono = None
    __carreras = None

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = ManejadorCarreras()

    
    def agregarCarrera(self, idCarrera, nombre, titulo, duracion, nivel):
        unaCarrera = Carrera(idCarrera, nombre, titulo, duracion, nivel)
        self.__carreras.agregarCarrera(unaCarrera)
    

    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getLocalidad(self):
        return self.__localidad


    def getFacultadCarreras(self):
        cadena = "Nombre: {0}\n".format(self.getNombre())
        cadena +=("{0:50}{1}".format("Nombre de carrera", "Duracion"))
        for unaCarrera in self.__carreras:
            cadena += "\n{0:50}{1}".format(unaCarrera.getNombre(), unaCarrera.getDuracion())
        return cadena
    

    def getFacultadCarrera(self, nombreCarrera):
        cadena = None
        unaCarrera = self.__carreras.getCarreraPorNombre(nombreCarrera)
        if isinstance(unaCarrera, Carrera):
            cadena = "Codigo: {0}-{1}\n".format(self.getCodigo(), unaCarrera.getCodigo())
            cadena += "Nombre de la facultad: {0}\n".format(self.getNombre())
            cadena += "Localidad: {0}".format(self.getLocalidad())
        return cadena