# 🎓 Guía de Ejecución y Defensa ante el Profesor

Esta nota te prepara tanto para correr el proyecto como para responder las preguntas típicas que un profesor universitario suele hacer al calificar.

---

## 💻 1. Comandos de Ejecución

### Interfaz Web (Recomendada)
```bash
cd /home/ltar/proyecto_divisibilidad
python3 app.py
```
Abre en tu navegador favorito:
👉 `http://127.0.0.1:5000`

### Consola Modular
```bash
python3 main.py
```

### Consola Secuencial (1 solo archivo)
```bash
python3 consola_secuencial.py
```

---

## ❓ 2. Preguntas Típicas del Profesor y Cómo Responder

### P1: "¿Por qué el algoritmo de la división no usa el operador `/` o `%`?"
* **Respuesta:** *"Porque el objetivo de la práctica es implementar el algoritmo constructivo formal mediante restas sucesivas, garantizando el cumplimiento del teorema $a = b \cdot q + r$ y asegurando que el residuo sea estrictamente positivo ($0 \le r < |b|$), incluso para enteros negativos."*

### P2: "¿Cómo garantiza el programa que una ecuación diofántica tiene solución?"
* **Respuesta:** *"Por el Teorema de Bézout. Primero calculamos el $\text{MCD}(a, b)$ usando el algoritmo de Euclides. Si el residuo de $c \pmod{\text{MCD}}$ es cero (es decir, el MCD divide a $c$), la ecuación tiene infinitas soluciones enteras; si no lo divide, es imposible encontrar soluciones enteras."*

### P3: "¿Por qué el cambio de base solo soporta hasta base 16 en esta versión?"
* **Respuesta:** *"Porque utilizamos un diccionario de caracteres estándar `0123456789ABCDEF` que cubre los sistemas numéricos más estudiados en computación (binario, octal, decimal y hexadecimal). Si se requirieran bases mayores (como base 64 o base 20), bastaría con extender la cadena de símbolos o representar los residuos numéricamente entre corchetes."*

### P4: "¿Por qué decidieron usar `http.server` en lugar de instalar un framework como Flask o Django?"
* **Respuesta:** *"Para mantener el proyecto ligero, portable y sin dependencias externas. Cualquier evaluador puede clonar el repositorio y ejecutarlo inmediatamente en cualquier entorno con Python 3 estándar, sin necesidad de configurar un entorno virtual (`venv`) ni ejecutar `pip install`."*

---

## 📊 3. Casos de Prueba Listos para Demostración

| Algoritmo | Datos de Entrada | Resultado a Mostrar |
| :--- | :--- | :--- |
| **División** | $a = 45, b = 6$ | Cociente = 7, Residuo = 3 ($45 = 6 \cdot 7 + 3$) |
| **División (Negativo)** | $a = -45, b = 6$ | Cociente = -8, Residuo = 3 ($-45 = 6 \cdot (-8) + 3$) |
| **Cambio de Base** | Número = 255, Base = 16 | $(FF)_{16}$ |
| **Cambio de Base** | Número = 43, Base = 2 | $(101011)_{2}$ |
| **MCD (Euclides)** | $a = 252, b = 105$ | $\text{MCD} = 21$ |
| **Diofántica (Con solución)** | $24x + 36y = 12$ | $\text{MCD} = 12$, Solución: $x = -1, y = 1$ |
| **Diofántica (Sin solución)** | $6x + 9y = 5$ | No tiene solución (el $\text{MCD} = 3$ no divide a $5$) |

---

Volver al índice: [[00-Indice-Principal]]
