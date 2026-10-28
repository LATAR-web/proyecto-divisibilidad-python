from interfaz import (
    limpiar_pantalla,
    mostrar_encabezado,
    mostrar_menu,
    mostrar_resultado_caja,
    pedir_entero,
    pausar
)
from algoritmos import (
    calcular_division,
    convertir_base,
    calcular_mcd,
    resolver_diofantica
)


# ciclo principal del menu en consola
def iniciar_programa():
    opcion = 0

    while opcion != 5:
        limpiar_pantalla()
        mostrar_menu()
        opcion = pedir_entero("Selecciona una opcion (1-5): ")

        if opcion == 1:
            mostrar_encabezado("1. ALGORITMO DE LA DIVISION")
            a = pedir_entero("Ingresa el dividendo (a): ")
            b = pedir_entero("Ingresa el divisor (b): ")
            res = calcular_division(a, b)
            mostrar_resultado_caja(res.split("  |  "))
            pausar()

        elif opcion == 2:
            mostrar_encabezado("2. CAMBIO DE BASE (b > 1)")
            num = pedir_entero("Ingresa el numero en base 10: ")
            base = pedir_entero("Ingresa la nueva base (b > 1): ")
            res = convertir_base(num, base)
            mostrar_resultado_caja([res])
            pausar()

        elif opcion == 3:
            mostrar_encabezado("3. MCD POR ALGORITMO DE EUCLIDES")
            a = pedir_entero("Ingresa el primer numero (a): ")
            b = pedir_entero("Ingresa el segundo numero (b): ")
            res = calcular_mcd(a, b)
            mostrar_resultado_caja([res])
            pausar()

        elif opcion == 4:
            mostrar_encabezado("4. ECUACIONES DIOFANTICAS (ax + by = c)")
            a = pedir_entero("Ingresa el valor de a: ")
            b = pedir_entero("Ingresa el valor de b: ")
            c = pedir_entero("Ingresa el valor de c: ")
            res = resolver_diofantica(a, b, c)
            mostrar_resultado_caja(res.split("  |  "))
            pausar()

        elif opcion == 5:
            print("\n  Saliendo del programa...")

        else:
            print("\n  Opcion no valida.")


if __name__ == "__main__":
    iniciar_programa()
