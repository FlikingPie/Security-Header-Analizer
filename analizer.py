import requests
import time
import shutil
import datetime
from pathlib import Path
from rich.progress import track
from rich import print
from rich.console import Console
from rich.theme import Theme
import re

# Content-Type, Content-Security-Policy, X-Frame-Options, Referrer-Policy

theme = Theme({
    "success": "green",
    "error": "red"
})

console = Console(theme=theme)

direcciones = input("Ingrese las direcciones URL: ").split()

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

headers_encontradas = []

fecha = datetime.datetime.now()


def progress_bar() -> None:
    for _ in track(range(10), description="GENERANDO CARPETA DE REPORTES..."):
        time.sleep(0.5)


def validaciones(direcciones: list) -> list:
    validadas = []

    try:
        for direccion in direcciones:
            print(f'Comprobando solicitud: {direccion}')
            response = requests.get(direccion,headers=HEADERS,timeout=6)
            status_code = response.status_code
            if 200 <= status_code < 400:
                console.print("Respuesta validada!! ✔\n", style="success")
                validadas.append((direccion, response))
            else:
                console.print("No se completo la conexión ✖", style="error")

    except KeyboardInterrupt:
        console.print("Error...Vuelva a intentar las conexiones!", style="error")
    except Exception as e:
        console.print(f'Error inesperado!!! {e}', style="error")

    return validadas


def validar_info():
    info = []
    contador = 0

    headers = [
        "Content-Type",
        "Content-Security-Policy-Report-Only",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "Cache-Control",
        "Content-Security-Policy",
        "Referrer-Policy"
    ]

    url_validadas = validaciones(direcciones)

    for validado, response in url_validadas:
        dataJson = dict(response.headers)
        info_header = []
        for i, header in enumerate(headers, start=1):
            if header in dataJson:
                console.print(f'[{i}] {header} ✔', style="success")
                info_header.append(header)
                contador += 1
            else:
                console.print(f"[{i}] No se encontro el header {header} ✖",style="error")

        info.append(info_header)
        headers_encontradas.append(contador)
        contador = 0

        print()
    return info


def generar_reportes():
    headers_totales = 8
    names = []

    results = validar_info()

    carpeta = Path("Carpeta de reportes")
    carpeta.mkdir(exist_ok=True)

    progress_bar()

    for direccion in direcciones:
        match = re.search(r"(?:https?://)?(?:www\.)?([^.]+)", direccion)
        if match:
            names.append(match.group(1))

    for name, result, encontrado in zip(names, results, headers_encontradas):
        archivo = f"Reporte_{name}.txt"
        with open(archivo, "w", encoding="utf-8") as file:
            file.write("=====================\n")
            file.write("      REPORTE\n")
            file.write("=====================\n\n")
            file.write(f"Fecha: {fecha.day}/{fecha.month}/{fecha.year}\n")
            file.write("--------------------------\n")
            file.write("\n".join(result))
            file.write(f"\n\nEncontrados: {encontrado}/{headers_totales}")

        shutil.move(archivo, carpeta / archivo)


generar_reportes()
