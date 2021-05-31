from ClaseSabor import Sabor
import csv

class ManejadorSabores:
    __listaSabores = []
    __listaVendidos = []

    def __init__(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo, delimiter=',')

        for fila in reader:
            d1 = int(fila[0])
            d2 = str(fila[1])
            d3 = str(fila[2])
            UnSabor = Sabor(d1, d2, d3)
            print(UnSabor)
            lista = [d2, 0]

            self.__listaVendidos.append(lista)
            self.__listaSabores.append(UnSabor)

    def BuscarSabor(self, nombreSabor):
        banderaRetun = False
        i = 0
        limite = len(self.__listaSabores)

        while (banderaRetun == False and i < limite):
            if (self.__listaSabores[i].GetNombre() == nombreSabor):
                self.__listaVendidos[i][1] += 1
                banderaRetun = True
            else:
                i += 1
        if (banderaRetun == True):
            banderaRetun = Sabor(self.__listaSabores[i].GetNumero(), self.__listaSabores[i].GetNombre(), self.__listaSabores[i].GetDescripcion)

        return (banderaRetun)

    def MostrarMasVendidos(self):
        print("MOSTRANDO VENTAS")

        limite = len(self.__listaVendidos)
        print(limite)
        i = 0
        while (i < limite):
            print(self.__listaVendidos[i])
            i += 1

