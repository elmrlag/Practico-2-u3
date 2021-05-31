class Sabor:
    __numero = 0
    __nombre = 0
    __descripcion = 0

    def __init__(self, v1 = 132, v2 = "granizado", v3 = "ta muy riko"):
        self.__numero = v1
        self.__nombre = v2
        self.__descripcion = v3

    def __str__(self):
        cadena = f"nombre: {self.__nombre}, numero: {self.__numero}, descripcion: {self.__descripcion}"
        return (cadena)

    def GetNombre(self):
        return self.__nombre

    def GetNumero(self):
        return self.__numero

    def GetDescripcion(self):
        return self.__descripcion