def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número entero válido.")


opcion = 0

# Menú principal del programa
while opcion != 5:
    print("\n--- MENÚ DE DIVISIBILIDAD Y ENTEROS ---")
    print("1. Algoritmo de la división")
    print("2. Cambio de base (2 <= b <= 16)")
    print("3. MCD por algoritmo de Euclides")
    print("4. Solución de ecuaciones Diofánticas")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opción (1-5): "))
    except ValueError:
        print("Opción no válida. Ingresa un número del 1 al 5.")
        continue

    # Parte 1: Algoritmo de la división (soporta positivos y negativos)
    if opcion == 1:
        n1 = pedir_entero("Ingresa el dividendo (a): ")
        n2 = pedir_entero("Ingresa el divisor (b): ")

        if n2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            q = 0
            r = abs(n1)
            d = abs(n2)

            while r >= d:
                r -= d
                q += 1

            if n1 < 0 and r > 0:
                r = d - r
                q = -(q + 1)
            elif n1 < 0:
                q = -q

            if n2 < 0:
                q = -q

            print(f"Cociente (q): {q}")
            print(f"Residuo (r): {r}")
            print(f"Comprobación: {n1} = ({n2}) * ({q}) + {r}")

    # Parte 2: Cambio de base
    elif opcion == 2:
        num = pedir_entero("Ingresa el número en base 10 (>= 0): ")
        b = pedir_entero("Ingresa la nueva base (2 a 16): ")

        if b < 2 or b > 16 or num < 0:
            print("Error: La base debe estar entre 2 y 16, y el número debe ser >= 0.")
        elif num == 0:
            print(f"El número 0 en base {b} es: 0")
        else:
            digitos = "0123456789ABCDEF"
            resultado = ""
            aux = num

            while aux > 0:
                residuo = aux % b
                resultado = digitos[residuo] + resultado
                aux = aux // b

            print(f"El número {num} en base {b} es: ({resultado}) base {b}")

    # Parte 3: MCD por Euclides
    elif opcion == 3:
        a = pedir_entero("Ingresa el primer número: ")
        b = pedir_entero("Ingresa el segundo número: ")

        if a == 0 and b == 0:
            print("Error: El MCD de 0 y 0 no existe.")
        else:
            x = abs(a)
            y = abs(b)

            while y != 0:
                residuo = x % y
                x = y
                y = residuo

            print(f"El MCD de {a} y {b} es: {x}")

    # Parte 4: Ecuaciones Diofánticas (ax + by = c)
    elif opcion == 4:
        a = pedir_entero("Ingresa el valor de a: ")
        b = pedir_entero("Ingresa el valor de b: ")
        c = pedir_entero("Ingresa el valor de c: ")

        if a == 0 and b == 0:
            print("Error: a y b no pueden ser ambos cero.")
        else:
            signo_a = -1 if a < 0 else 1
            signo_b = -1 if b < 0 else 1

            r0, r1 = abs(a), abs(b)
            s0, s1 = 1, 0
            t0, t1 = 0, 1

            while r1 != 0:
                cociente = r0 // r1
                r0, r1 = r1, r0 - cociente * r1
                s0, s1 = s1, s0 - cociente * s1
                t0, t1 = t1, t0 - cociente * t1

            mcd = r0

            if c % mcd != 0:
                print(f"No tiene solución entera porque el MCD ({mcd}) no divide a {c}.")
            else:
                factor = c // mcd
                x0 = s0 * factor * signo_a
                y0 = t0 * factor * signo_b
                print(f"MCD: {mcd}")
                print(f"Solución particular: x = {x0}, y = {y0}")
                print(f"Comprobación: ({a})({x0}) + ({b})({y0}) = {c}")

    elif opcion == 5:
        print("Saliendo del programa...")

    else:
        print("Opción no válida. Elige un número del 1 al 5.")