# 🏗️ Arquitectura General del Proyecto

Este documento explica cómo está organizado el proyecto y el flujo de ejecución entre los diferentes archivos.

---

## 📂 Árbol de Archivos

```text
proyecto_divisibilidad/
├── algoritmos.py            # El núcleo lógico y matemático del sistema
├── app.py                   # Servidor web nativo (Backend HTTP)
├── main.py                  # Punto de entrada para ejecución por terminal (modular)
├── interfaz.py              # Funciones visuales para terminal (cajas, pausas, limpiar)
├── consola_secuencial.py    # Versión básica alternativa (todo en 1 archivo)
├── templates/
│   └── index.html           # Estructura visual de las 4 pestañas/tarjetas
├── static/
│   └── estilos.css          # Estilos visuales y animaciones fluidas
├── documentacion_obsidian/  # Notas para Obsidian
├── .gitignore               # Exclusiones de Git
└── README.md                # Presentación del repositorio
```

---

## 🔄 Flujo de Datos en la Aplicación Web

```
[ Usuario en Navegador ]
         │ (Escribe números en el formulario)
         ▼
[ templates/index.html ]
         │ (JavaScript captura el evento 'submit' y usa fetch('/'))
         ▼
[ app.py (Servidor HTTP) ]
         │ (do_POST lee los datos y llama a la función correspondiente)
         ▼
[ algoritmos.py ]
         │ (Calcula con ciclos básicos y devuelve un texto formateado)
         ▲
[ app.py ]
         │ (Devuelve JSON: {"opcion": "...", "resultado": "..."})
         ▼
[ index.html + estilos.css ]
         ▼ (Se inyecta el resultado y se activa la clase '.mostrar')
[ Despliegue animado debajo del botón ]
```

---

## 🧩 Funcionalidad de Cada Archivo

### 1. `algoritmos.py`
Contiene las cuatro funciones puras:
* `calcular_division(a, b)`
* `convertir_base(numero, base)`
* `calcular_mcd(a, b)`
* `resolver_diofantica(a, b, c)`

No tiene interacción con el usuario (`input` o `print`), lo que permite que sea reutilizado tanto por la **web** como por la **consola**.

### 2. `app.py`
Usa la biblioteca estándar `http.server` y `HTTPServer`:
* Atiende peticiones `GET` para servir el HTML y el CSS.
* Atiende peticiones `POST` cuando el usuario hace clic en "Calcular".
* No requiere `pip install flask`, garantizando que funcione en cualquier computadora con Python 3 instalado.

### 3. `templates/index.html` y `static/estilos.css`
Diseñado para verse profesional pero entendible para un estudiante universitario:
* Contenedor en cuadrícula (`CSS Grid`) para que las 4 tarjetas se adapten a cualquier pantalla.
* Animación fluida de acordeón para que el resultado aparezca suavemente debajo del botón correspondiente.

---

Siguiente lectura recomendada: [[02-Matematicas-y-Algoritmos]]
