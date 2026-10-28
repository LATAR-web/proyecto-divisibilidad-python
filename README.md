# Proyecto: Programación en Python de Divisibilidad y Números Enteros

Proyecto universitario desarrollado en **Python** con interfaz web en **HTML y CSS** y versión en consola, enfocado en la implementación de algoritmos fundamentales de divisibilidad y números enteros.

---

## Descripción del Proyecto

Este programa resuelve cuatro problemas de la materia de **Matemáticas Discretas / Álgebra Superior**:

1. **Algoritmo de la división:** Obtiene el cociente ($q$) y el residuo ($r$) de dos números enteros tales que $a = b \cdot q + r$ con $0 \le r < |b|$.
2. **Cambio de base ($b > 1$):** Convierte un número entero positivo en base 10 a su representación en cualquier base $b > 1$ mediante divisiones sucesivas.
3. **Máximo Común Divisor (MCD):** Calcula el MCD de dos números enteros implementando el **Algoritmo de Euclides**.
4. **Solución de Ecuaciones Diofánticas:** Determina si una ecuación lineal de la forma $ax + by = c$ tiene soluciones enteras utilizando el **Algoritmo de Euclides Extendido** y calcula su solución particular.

---

## Estructura del Repositorio

```text
proyecto_divisibilidad/
├── static/
│   └── estilos.css          # Estilos CSS de la interfaz web
├── templates/
│   └── index.html           # Interfaz web con el menú de las 4 partes
├── algoritmos.py            # Funciones matemáticas de los 4 algoritmos
├── app.py                   # Servidor local en Python que conecta el HTML con los algoritmos
├── main.py                  # Menú principal para ejecutar en consola modular
├── interfaz.py              # Funciones de apoyo para el menú en consola
├── consola_secuencial.py    # Versión alternativa en un solo archivo para consola
├── .gitignore               # Archivos ignorados por Git
└── README.md                # Documentación del proyecto
```

---

## Cómo Ejecutar el Proyecto

### Opción 1: Interfaz Web (HTML + CSS + Python)

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/LATAR-web/proyecto-divisibilidad-python.git
   cd proyecto-divisibilidad-python
   ```
2. Ejecutar el servidor local:
   ```bash
   python3 app.py
   ```
3. Abrir en el navegador:
   ```text
   http://127.0.0.1:5000
   ```

### Opción 2: Versión en Consola

Para ejecutar el menú en la terminal:
```bash
python3 main.py
```
O la versión secuencial en un solo archivo:
```bash
python3 consola_secuencial.py
```

---

## Ejemplos de Prueba

| Parte | Entrada de prueba | Resultado esperado |
| :--- | :--- | :--- |
| **1. División** | $a = 45, b = 6$ | Cociente $q = 7$, Residuo $r = 3$ ($45 = 6 \cdot 7 + 3$) |
| **2. Cambio de base** | Número $= 255$, Base $= 16$ | $(FF)_{16}$ |
| **3. MCD (Euclides)** | $a = 252, b = 105$ | $\text{MCD}(252, 105) = 21$ |
| **4. Ec. Diofántica** | $24x + 36y = 12$ | $\text{MCD} = 12$, Solución: $x = -1, y = 1$ |
