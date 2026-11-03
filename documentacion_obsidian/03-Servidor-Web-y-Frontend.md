# 🌐 Servidor Web y Frontend

En esta nota se explica cómo se construyó la interfaz web y la comunicación cliente-servidor sin usar librerías externas pesadas.

---

## ⚙️ 1. Backend: Python Nativo (`http.server`)

En proyectos universitarios, los profesores a veces revisan el código en computadoras donde no pueden o no quieren instalar paquetes vía `pip`.

Por esta razón, en lugar de frameworks como Django o Flask, se utilizó el módulo nativo de Python:
```python
from http.server import HTTPServer, BaseHTTPRequestHandler
```

### Rutas Gestionadas
* **`do_GET(self)`**:
  * Si la ruta solicitada es `/static/estilos.css`, responde con el archivo CSS y la cabecera `Content-type: text/css`.
  * Cualquier otra petición sirve el archivo `templates/index.html`.
* **`do_POST(self)`**:
  * Lee el cuerpo de la petición (`self.rfile.read`).
  * Parsea los datos con `urllib.parse.parse_qs`.
  * Invoca a la función en `algoritmos.py`.
  * Responde con un objeto JSON:
    ```json
    {
      "opcion": "1",
      "resultado": "Cociente (q) = 7 | Residuo (r) = 3 | Comprobacion: 45 = (6)*(7) + 3"
    }
    ```

---

## 🎨 2. Frontend: HTML5 y CSS3

### Maquetación con CSS Grid
Para mostrar las 4 opciones del menú de forma balanceada:
```css
.cuadricula {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 22px;
}
```
Esto asegura que en monitores grandes se vean 2 columnas y en teléfonos o pantallas pequeñas se acomode automáticamente a 1 columna.

### Animación de la Caja de Respuestas
El truco para que la respuesta no aparezca de golpe ni empuje la pantalla bruscamente:

```css
.caja-resultado {
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transform: translateY(-8px);
    transition: all 0.35s ease;
}

.caja-resultado.mostrar {
    max-height: 180px;
    opacity: 1;
    transform: translateY(0);
}
```

---

## ⚡ 3. Comunicación Asíncrona con `fetch`

En `templates/index.html` se usa JavaScript básico para evitar que la página se recargue por completo cada vez que se presiona "Calcular":

```javascript
form.addEventListener('submit', async function(evento) {
    evento.preventDefault(); // Evita recarga completa

    const respuesta = await fetch('/', {
        method: 'POST',
        headers: { 'X-Requested-With': 'fetch' },
        body: new URLSearchParams(new FormData(form)).toString()
    });

    const datosJson = await respuesta.json();
    caja.innerHTML = '<strong>Resultado:</strong><br>' + datosJson.resultado.replaceAll('  |  ', '<br>');
    caja.classList.add('mostrar'); // Activa la animación CSS
});
```

---

Siguiente lectura recomendada: [[04-Guia-de-Ejecucion-y-Defensa]]
