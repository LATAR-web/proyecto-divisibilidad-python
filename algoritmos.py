# Parte 1: Algoritmo de la división
def calcular_division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."

    q = 0
    r = abs(a)
    d = abs(b)

    # restamos el divisor hasta que el residuo sea menor
    while r >= d:
        r = r - d
        q = q + 1

    # ajuste de signos para cumplir 0 <= r < |b|
    if a < 0 and r > 0:
        r = d - r
        q = -(q + 1)
    elif a < 0:
        q = -q

    if b < 0:
        q = -q

    return f"Cociente (q) = {q}  |  Residuo (r) = {r}  |  Comprobación: {a} = ({b})*({q}) + {r}"


# Parte 2: Cambio de base
def convertir_base(numero, base):
    if base < 2 or base > 16:
        return "Error: La base debe estar entre 2 y 16."

    if numero < 0:
        return "Error: Ingresa un número entero no negativo (>= 0)."

    if numero == 0:
        return f"El número 0 en base {base} es: 0"

    digitos = "0123456789ABCDEF"
    resultado = ""
    aux = numero

    # divisiones sucesivas entre la base
    while aux > 0:
        residuo = aux % base
        resultado = digitos[residuo] + resultado
        aux = aux // base

    return f"El número {numero} en base {base} es: ({resultado}) base {base}"


# Parte 3: MCD con el algoritmo de Euclides
def calcular_mcd(a, b):
    if a == 0 and b == 0:
        return "Error: El MCD de 0 y 0 no existe."

    x = abs(a)
    y = abs(b)

    # sacamos el residuo hasta llegar a cero
    while y != 0:
        residuo = x % y
        x = y
        y = residuo

    return f"El MCD de {a} y {b} es: {x}"


# Parte 4: Solución de ecuaciones diofánticas
def resolver_diofantica(a, b, c):
    if a == 0 and b == 0:
        return "Error: a y b no pueden ser cero al mismo tiempo."

    # Se obtienen los signos iniciales para trabajar con absolutos en Euclides
    signo_a = -1 if a < 0 else 1
    signo_b = -1 if b < 0 else 1

    r0, r1 = abs(a), abs(b)
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    # Algoritmo de Euclides Extendido
    while r1 != 0:
        cociente = r0 // r1

        r0, r1 = r1, r0 - cociente * r1
        s0, s1 = s1, s0 - cociente * s1
        t0, t1 = t1, t0 - cociente * t1

    mcd = r0

    # Solo tiene solución si el MCD divide a c
    if c % mcd != 0:
        return f"No tiene solución entera porque el MCD ({mcd}) no divide a {c}."

    factor = c // mcd
    x0 = s0 * factor * signo_a
    y0 = t0 * factor * signo_b

    return f"MCD = {mcd}  |  Solución particular: x = {x0}, y = {y0}  |  Comprobación: ({a})({x0}) + ({b})({y0}) = {c}"