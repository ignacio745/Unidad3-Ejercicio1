from Facultad import Facultad
import csv

class ManejadorFacultades:
    __facultades = None

    def __init__(self):
        self.__facultades = []
    
    def agregarFacultad(self, unaFacultad):
        if isinstance(unaFacultad, Facultad):
            self.__facultades.append(unaFacultad)


    def cargarFacultades(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=';')
        band = True
        filaFacultad = next(reader)
        while band:
            band2 = True
            while band2:
                try:
                    unaFacultad = Facultad(int(filaFacultad[0]), filaFacultad[1], filaFacultad[2], filaFacultad[3], filaFacultad[4])
                except:
                    try:
                        filaFacultad = next(reader)
                    except StopIteration:
                        band = False
                        band2 = False
                else:
                    self.agregarFacultad(unaFacultad)
                    band2 = False
            try:
                filaCarrera = next(reader)
            except StopIteration:
                band = False
            while band and filaCarrera[0] == filaFacultad[0]:
                unaFacultad.agregarCarrera(int(filaCarrera[1]), filaCarrera[2], filaCarrera[3], filaCarrera[4], filaCarrera[5])
                try:
                    filaCarrera = next(reader)
                except StopIteration:
                    band = False
            filaFacultad = filaCarrera[0:-1]
        archivo.close()
    

    def buscarFacultad(self, codigo):
        i = 0
        while i < len(self.__facultades) and codigo != self.__facultades[i].getCodigo():
            i += 1
        if i == len(self.__facultades):
            i = -1
        return i


    def mostrarFacultadPorCodigo(self, codigo):
        indice = self.buscarFacultad(codigo)
        if indice != -1:
            print(self.__facultades[indice].getFacultadCarreras())
        else:
            print("[ERROR] No se encontro la facultad")
    

    def mostrarCarreraPorNombre(self, nombreCarrera):
        i = 0
        band = True
        while i < len(self.__facultades) and band:
            cadena = self.__facultades[i].getFacultadCarrera(nombreCarrera)
            if cadena == None:
                i += 1
            else:
                band = False
        if i == len(self.__facultades):
            print("[ERROR] No se encontro la carrera")
        else:
            print(cadena)