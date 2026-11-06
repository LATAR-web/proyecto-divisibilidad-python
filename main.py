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


# Ciclo principal del menú en consola
def iniciar_programa():
    opcion = 0

    while opcion != 5:
        limpiar_pantalla()
        mostrar_menu()
        opcion = pedir_entero("Selecciona una opción (1-5): ")

        if opcion == 1:
            mostrar_encabezado("1. ALGORITMO DE LA DIVISIÓN")
            a = pedir_entero("Ingresa el dividendo (a): ")
            b = pedir_entero("Ingresa el divisor (b): ")
            res = calcular_division(a, b)
            mostrar_resultado_caja(res.split("  |  "))
            pausar()

        elif opcion == 2:
            mostrar_encabezado("2. CAMBIO DE BASE (2 <= b <= 16)")
            num = pedir_entero("Ingresa el número en base 10: ")
            base = pedir_entero("Ingresa la nueva base (2 a 16): ")
            res = convertir_base(num, base)
            mostrar_resultado_caja([res])
            pausar()

        elif opcion == 3:
            mostrar_encabezado("3. MCD POR ALGORITMO DE EUCLIDES")
            a = pedir_entero("Ingresa el primer número (a): ")
            b = pedir_entero("Ingresa el segundo número (b): ")
            res = calcular_mcd(a, b)
            mostrar_resultado_caja([res])
            pausar()

        elif opcion == 4:
            mostrar_encabezado("4. ECUACIONES DIOFÁNTICAS (ax + by = c)")
            a = pedir_entero("Ingresa el valor de a: ")
            b = pedir_entero("Ingresa el valor de b: ")
            c = pedir_entero("Ingresa el valor de c: ")
            res = resolver_diofantica(a, b, c)
            mostrar_resultado_caja(res.split("  |  "))
            pausar()

        elif opcion == 5:
            print("\n  Saliendo del programa...")

        else:
            print("\n  Opción no válida.")
            pausar()


if __name__ == "__main__":
    iniciar_programa()