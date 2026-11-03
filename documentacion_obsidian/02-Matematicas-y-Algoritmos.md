# 🔢 Matemáticas y Algoritmos Explicados

En este documento se analiza la lógica matemática detrás de cada una de las 4 partes del proyecto, ubicadas en `algoritmos.py`.

---

## 1. Algoritmo de la División

### Fundamento Teórico
Para cualquier par de enteros $a$ (dividendo) y $b$ (divisor, con $b \neq 0$), existen enteros únicos $q$ (cociente) y $r$ (residuo) tales que:
$$a = b \cdot q + r \quad \text{donde} \quad 0 \le r < |b|$$

### Lógica en Python
En lugar de usar directamente los operadores `/` o `%`, el programa utiliza **restas sucesivas** para demostrar el funcionamiento algorítmico básico:

```python
q = 0
r = abs(a)
d = abs(b)

# Restamos el divisor tantas veces como quepa en el residuo
while r >= d:
    r = r - d
    q = q + 1
```

> [!NOTE] Manejo de Signos Negativos
> El residuo $r$ siempre debe ser estrictamente no-negativo ($0 \le r < |b|$). Por eso, si el dividendo original era negativo y sobró residuo ($r > 0$), se realiza el ajuste canónico:
> $$r = d - r$$
> $$q = -(q + 1)$$

---

## 2. Cambio de Base ($b > 1$)

### Fundamento Teórico
Cualquier entero positivo $n$ se puede descomponer en potencias de una base $b > 1$:
$$n = a_k b^k + a_{k-1} b^{k-1} + \dots + a_1 b + a_0$$
Los dígitos en la nueva base corresponden a los residuos sucesivos de dividir $n$ entre $b$.

### Lógica en Python
Se implementa un ciclo `while` donde se toman residuos con `%` y se actualiza el cociente con `//`:

```python
digitos = "0123456789ABCDEF"
resultado = ""
aux = numero

while aux > 0:
    residuo = aux % base
    resultado = digitos[residuo] + resultado # Se concatena hacia la izquierda
    aux = aux // base
```

---

## 3. Máximo Común Divisor (Algoritmo de Euclides)

### Fundamento Teórico
El algoritmo se basa en la propiedad fundamental de divisibilidad:
$$\text{MCD}(a, b) = \text{MCD}(b, a \pmod b)$$
Cuando el residuo llega a $0$, el último divisor no nulo es el MCD.

### Lógica en Python
```python
x = abs(a)
y = abs(b)

while y != 0:
    residuo = x % y
    x = y
    y = residuo
# Al salir del ciclo, x es el MCD
```

---

## 4. Solución de Ecuaciones Diofánticas

### Fundamento Teórico
Una ecuación diofántica lineal tiene la forma:
$$ax + by = c$$

Por el **Teorema de Bézout**:
1. La ecuación tiene solución entera **si y solo si** $\text{MCD}(a, b)$ divide a $c$ ($d \mid c$).
2. El **Algoritmo de Euclides Extendido** calcula enteros $s$ y $t$ tales que:
   $$as + bt = \text{MCD}(a, b)$$
3. Multiplicando toda la ecuación por el factor $k = \frac{c}{\text{MCD}(a, b)}$, se obtiene la solución particular $(x_0, y_0)$:
   $$x_0 = s \cdot \left(\frac{c}{\text{MCD}}\right), \quad y_0 = t \cdot \left(\frac{c}{\text{MCD}}\right)$$

### Lógica en Python
Se actualizan simultáneamente los residuos y los coeficientes de combinación lineal:

```python
while r1 != 0:
    cociente = r0 // r1
    # Actualización de residuos
    r0, r1 = r1, r0 - cociente * r1
    # Coeficiente para 'a' (s)
    s0, s1 = s1, s0 - cociente * s1
    # Coeficiente para 'b' (t)
    t0, t1 = t1, t0 - cociente * t1
```

---

Siguiente lectura recomendada: [[03-Servidor-Web-y-Frontend]]
