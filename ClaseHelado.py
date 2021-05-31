from ClaseSabor import Sabor

class Helado:
    __gramos = 0
    __listaSabor = []

    def __init__(self, v1 = 100):
        self.__gramos = v1
        self.__listaSabor = []

    def GetGramos(self):
        return self.__gramos

    def GetSabores(self):
        return self.__listaSabor

    def AgregarSabor(self, sabor):
        self.__listaSabor.append(sabor)

    def BuscarSabor(self, nombreSabor):
        encontrado = False
        limite = len(self.__listaSabor)
        i = 0

        while (i < limite and encontrado == False):
            if (self.__listaSabor[i].GetNombre == nombreSabor):
                encontrado = True
            else:
                i += 1

        return encontrado

    def SumarGramos(self, nombreSabor):
        gramos = 0
        limite = len(self.__listaSabor)
        i = 0

        while (i < limite):
            if (self.__listaSabor[i].GetNombre == nombreSabor):
                gramos += self.__gramos/limite
            i += 1

        return (gramos)