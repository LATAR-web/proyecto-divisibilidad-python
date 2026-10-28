import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from algoritmos import (
    calcular_division,
    convertir_base,
    calcular_mcd,
    resolver_diofantica
)


# lee el archivo html
def cargar_pagina():
    with open("templates/index.html", "r", encoding="utf-8") as archivo:
        return archivo.read()


# revisa que opcion se eligio y llama a la funcion correspondiente
def ejecutar_algoritmo(formulario):
    opcion = formulario.get("opcion", ["1"])[0]
    resultado = ""

    if opcion == "1":
        a = int(formulario["dividendo"][0])
        b = int(formulario["divisor"][0])
        resultado = calcular_division(a, b)

    elif opcion == "2":
        num = int(formulario["numero"][0])
        base = int(formulario["base"][0])
        resultado = convertir_base(num, base)

    elif opcion == "3":
        a = int(formulario["num_a"][0])
        b = int(formulario["num_b"][0])
        resultado = calcular_mcd(a, b)

    elif opcion == "4":
        a = int(formulario["coef_a"][0])
        b = int(formulario["coef_b"][0])
        c = int(formulario["coef_c"][0])
        resultado = resolver_diofantica(a, b, c)

    return opcion, resultado


class ServidorDivisibilidad(BaseHTTPRequestHandler):

    # carga la pagina y los estilos css
    def do_GET(self):
        if self.path == "/static/estilos.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css; charset=utf-8")
            self.end_headers()
            with open("static/estilos.css", "rb") as css:
                self.wfile.write(css.read())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            pagina = cargar_pagina()
            self.wfile.write(pagina.encode("utf-8"))

    # recibe los datos del formulario y regresa el resultado
    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        datos_bytes = self.rfile.read(longitud).decode("utf-8")
        formulario = parse_qs(datos_bytes)

        opcion, resultado = ejecutar_algoritmo(formulario)

        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        respuesta_json = json.dumps({"opcion": opcion, "resultado": resultado})
        self.wfile.write(respuesta_json.encode("utf-8"))


# inicia el servidor local en el puerto 5000
if __name__ == "__main__":
    puerto = 5000
    HTTPServer.allow_reuse_address = True
    try:
        servidor = HTTPServer(("127.0.0.1", puerto), ServidorDivisibilidad)
    except OSError:
        puerto = 5001
        servidor = HTTPServer(("127.0.0.1", puerto), ServidorDivisibilidad)

    print(f"Servidor iniciado en: http://127.0.0.1:{puerto}")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        servidor.server_close()
