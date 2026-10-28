import os


# limpia la consola
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


# muestra el titulo de cada parte
def mostrar_encabezado(titulo):
    ancho = 54
    print("\n+" + "-" * ancho + "+")
    print("|" + titulo.center(ancho) + "|")
    print("+" + "-" * ancho + "+")


# encierra el resultado en un cuadro
def mostrar_resultado_caja(lineas):
    ancho = 54
    print("\n+" + "-" * ancho + "+")
    for linea in lineas:
        print("|  " + linea.ljust(ancho - 2) + "|")
    print("+" + "-" * ancho + "+")


# imprime las opciones del menu
def mostrar_menu():
    mostrar_encabezado("PROYECTO: DIVISIBILIDAD Y NUMEROS ENTEROS")
    print("  1. Algoritmo de la Division")
    print("  2. Cambio de Base (b > 1)")
    print("  3. MCD por Algoritmo de Euclides")
    print("  4. Solucion de Ecuaciones Diofanticas")
    print("  5. Salir")


# valida que el usuario ingrese un numero entero
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input("  " + mensaje))
            return valor
        except ValueError:
            print("  Error: Ingresa un numero entero valido.")


def pausar():
    input("\n  Presiona Enter para continuar...")
