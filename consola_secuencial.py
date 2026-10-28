opcion = 0

# menu principal del programa
while opcion != 5:
    print("\n--- MENU DE DIVISIBILIDAD Y ENTEROS ---")
    print("1. Algoritmo de la division")
    print("2. Cambio de base (b > 1)")
    print("3. MCD por algoritmo de Euclides")
    print("4. Solucion de ecuaciones Diofanticas")
    print("5. Salir")

    opcion = int(input("Elige una opcion (1-5): "))

    # parte 1: algoritmo de la division
    if opcion == 1:
        n1 = int(input("Ingresa el dividendo (a): "))
        n2 = int(input("Ingresa el divisor (b): "))

        if n2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            q = 0
            r = n1
            while r >= n2:
                r = r - n2
                q = q + 1
            print("Cociente (q):", q)
            print("Residuo (r):", r)
            print("Comprobacion:", n1, "=", n2, "*", q, "+", r)

    # parte 2: cambio de base
    elif opcion == 2:
        num = int(input("Ingresa el numero en base 10: "))
        b = int(input("Ingresa la nueva base (b > 1): "))

        if b <= 1 or num < 0:
            print("Error: La base debe ser mayor a 1 y el numero positivo.")
        elif num == 0:
            print("El numero en base", b, "es: 0")
        else:
            digitos = "0123456789ABCDEF"
            resultado = ""
            aux = num

            while aux > 0:
                residuo = aux % b
                resultado = digitos[residuo] + resultado
                aux = aux // b

            print("El numero", num, "en base", b, "es:", resultado)

    # parte 3: mcd por euclides
    elif opcion == 3:
        a = int(input("Ingresa el primer numero: "))
        b = int(input("Ingresa el segundo numero: "))

        if a == 0 and b == 0:
            print("Error: El MCD de 0 y 0 no existe.")
        else:
            x = abs(a)
            y = abs(b)

            while y != 0:
                residuo = x % y
                x = y
                y = residuo

            print("El MCD de", a, "y", b, "es:", x)

    # parte 4: ecuaciones diofanticas
    elif opcion == 4:
        a = int(input("Ingresa el valor de a: "))
        b = int(input("Ingresa el valor de b: "))
        c = int(input("Ingresa el valor de c: "))

        if a == 0 and b == 0:
            print("Error: a y b no pueden ser ambos cero.")
        else:
            r0 = a
            r1 = b
            s0 = 1
            s1 = 0
            t0 = 0
            t1 = 1

            while r1 != 0:
                cociente = r0 // r1

                temp_r = r0 - cociente * r1
                r0 = r1
                r1 = temp_r

                temp_s = s0 - cociente * s1
                s0 = s1
                s1 = temp_s

                temp_t = t0 - cociente * t1
                t0 = t1
                t1 = temp_t

            mcd = r0

            if c % mcd != 0:
                print("No tiene solucion entera porque", mcd, "no divide a", c)
            else:
                factor = c // mcd
                x0 = s0 * factor
                y0 = t0 * factor
                print("MCD:", abs(mcd))
                print("Solucion: x =", x0, ", y =", y0)

    elif opcion == 5:
        print("Saliendo...")
    else:
        print("Opcion no valida.")
