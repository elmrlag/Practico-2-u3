from ClaseManejadorHelados import ManejadorHelados
from ClaseManejadorSabores import ManejadorSabores

def opcion0():
    print("Saliendo")

def opcion1():
    MHelados.RegistrarVentaHelado(MSabores)

def opcion2():
    MSabores.MostrarMasVendidos()

def opcion3():
    MHelados.CalcularVentaSabores(MSabores)

def opcion4():
    MHelados.BuscarSaboresVendidoEnGramos()

switcher ={
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opcion incorrecta"))
    func()

if __name__=='__main__':

    MHelados = ManejadorHelados()
    MSabores = ManejadorSabores()
    bandera = False


    while not bandera:
        print("MENU DE OPCIONES")
        print("0 para salir")
        print("1 para Registrar un helado vendido")
        print("2 para Mostrar el nombre de los 5 sabores de helado más pedido")
        print("3 para Ingresar un número de sabor y estimar el total de gramos vendidos")
        print("4 para Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño")
        opcion = int(input("Ingrese valor: "))
        switch(opcion)
        bandera = int(opcion) == 0