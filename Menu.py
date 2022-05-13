from ManejadorFacultades import ManejadorFacultades
from IngresadorTeclado import IngresadorTeclado


class Menu:
    __switcher=None
    __ingresador = None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.salir
                          }
        self.__ingresador = IngresadorTeclado()
    def opcion(self, unManejadorFacultades, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op =='2':
            func(unManejadorFacultades)
        elif op =='3':
            func()
        else:
            func()
    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, unManejadorFacultades):
        if isinstance(unManejadorFacultades, ManejadorFacultades):
            codigo = self.__ingresador.inputInt("Ingrese el codigo de la facultad: ")
            unManejadorFacultades.mostrarFacultadPorCodigo(codigo)
        


    def opcion2(self, unManejadorFacultades):
        if isinstance(unManejadorFacultades, ManejadorFacultades):
            carrera = input("Ingrese el nombre de la carrera: ")
            unManejadorFacultades.mostrarCarreraPorNombre(carrera)


    def ejecutarMenu(self, unManejadorFacultades):
        if isinstance(unManejadorFacultades, ManejadorFacultades):
            opcion = "0"
            while opcion != "3":
                print("Ingrese la opcion deseada")
                print("[1] Mostrar carreras por codigo de facultad")
                print("[2] Mostrar facultad de una carrera dado su nombre")
                print("[3] Salir")
                opcion = input("--> ")  
                self.opcion(unManejadorFacultades, opcion)
