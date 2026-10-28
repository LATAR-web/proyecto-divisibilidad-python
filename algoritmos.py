# Parte 1: Algoritmo de la division
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

    # ajuste de signos si el dividendo o divisor son negativos
    if a < 0 and r > 0:
        r = d - r
        q = -(q + 1)
    elif a < 0:
        q = -q

    if b < 0:
        q = -q

    return f"Cociente (q) = {q}  |  Residuo (r) = {r}  |  Comprobacion: {a} = ({b})*({q}) + {r}"


# Parte 2: Cambio de base
def convertir_base(numero, base):
    if base <= 1:
        return "Error: La base debe ser mayor a 1."

    if numero < 0:
        return "Error: Ingresa un numero positivo."

    if numero == 0:
        return f"0 en base {base} es: 0"

    digitos = "0123456789ABCDEF"
    resultado = ""
    aux = numero

    # divisiones sucesivas entre la base
    while aux > 0:
        residuo = aux % base
        resultado = digitos[residuo] + resultado
        aux = aux // base

    return f"El numero {numero} en base {base} es: ({resultado}) base {base}"


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


# Parte 4: Solucion de ecuaciones diofanticas
def resolver_diofantica(a, b, c):
    if a == 0 and b == 0:
        return "Error: a y b no pueden ser cero al mismo tiempo."

    r0 = a
    r1 = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1

    # algoritmo de Euclides extendido para sacar x, y
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

    # solo tiene solucion si el mcd divide a c
    if c % mcd != 0:
        return f"No tiene solucion entera porque el MCD ({abs(mcd)}) no divide a {c}."

    factor = c // mcd
    x0 = s0 * factor
    y0 = t0 * factor

    return f"MCD = {abs(mcd)}  |  Solucion: x = {x0}, y = {y0}  |  Comprobacion: ({a})({x0}) + ({b})({y0}) = {c}"
