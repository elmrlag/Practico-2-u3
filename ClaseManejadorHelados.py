from ClaseHelado import Helado
from ClaseSabor import Sabor
from ClaseManejadorSabores import ManejadorSabores

class ManejadorHelados:
    __listaHelados = []

    def __init__(self):
        self.__listaHelados = []

    def RegistrarVentaHelado(self, MSabores):
        print("INICIO DE VENTA DE HELADO")

        gramos = int(input("Gramos del helado pedido: "))
        UnHelado = Helado(gramos)

        banderaSabores = True
        while (banderaSabores == True):
            nombreSabor = str(input("Nombre del sabor: "))

            encontrado = MSabores.BuscarSabor(nombreSabor)
            if (encontrado == False):
                print("Sabor no encontrado, ingrese otro")

            else:
                UnHelado.AgregarSabor(encontrado)

                print("desea otro sabor?")
                respuesta = -1
                while(respuesta != 1 and respuesta != 0):
                    respuesta = int(input("0: NO o 1: SI"))
                    if (respuesta != 1 and respuesta != 0):
                        print("respuesta incorrecta, opcion 0 o 1")
                if (respuesta == 1):
                    banderaSabores = True
                else:
                    self.__listaHelados.append(UnHelado)
                    banderaSabores = False

    def CalcularVentaSabores(self, MSabores):
        nombreSabor = str(input("Nombre del sabor: "))
        encontrado = False
        while (encontrado == False):
            encontrado = MSabores.BuscarSabor(nombreSabor)
            if (encontrado == False):
                print("Sabor no encontrado, ingrese otro")

            else:
                cont = 0
                limite = len(self.__listaHelados)
                i = 0
                while(i < limite):
                    saborEncontrado = self.__listaHelados[i].BuscarSabor(nombreSabor)
                    if (saborEncontrado == True):
                        cont += self.__listaHelados[i].SumarGramos(nombreSabor)
                    i += 0
                print(f"los gramos totales del sabor -{nombreSabor}- es de: {cont}gr")

    def BuscarSaboresVendidoEnGramos(self):
        gramos = int(input("ingrese gramos: "))

        limite = len(self.__listaHelados)
        i = 0
        listaSabores = []
        while (i < limite):
            if (gramos == self.__listaHelados[i].GetGramos()):
                listaSabores.append(self.__listaHelados[i].GetSabores())
        print(listaSabores)

