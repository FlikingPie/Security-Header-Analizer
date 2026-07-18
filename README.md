# 🔒 HTTP Security Headers Analyzer

## 📖 Descripción

**HTTP Security Headers Analyzer** es una herramienta desarrollada en Python que permite analizar la presencia de cabeceras HTTP de seguridad en uno o varios sitios web.

El programa solicita al usuario una lista de direcciones URL, verifica que cada sitio responda correctamente y analiza la existencia de distintas cabeceras HTTP relacionadas con la seguridad. Finalmente, genera un reporte individual para cada sitio y los almacena en una carpeta llamada **Carpeta de reportes**.

---

# ✨ Características

* Analiza una o varias URL ingresadas por el usuario.
* Verifica que cada sitio responda correctamente antes del análisis.
* Comprueba la existencia de ocho cabeceras HTTP de seguridad.
* Muestra los resultados en consola utilizando la librería **Rich**.
* Genera un reporte independiente para cada sitio analizado.
* Organiza automáticamente los reportes dentro de una carpeta.
* Incluye una barra de progreso durante la generación de los reportes.
* Utiliza un **User-Agent** personalizado y un **timeout** para mejorar la compatibilidad con distintos servidores.

---

# 🔍 Cabeceras HTTP analizadas

El programa verifica las siguientes cabeceras:

* Content-Type
* Content-Security-Policy
* Content-Security-Policy-Report-Only
* X-Frame-Options
* X-Content-Type-Options
* Strict-Transport-Security
* Cache-Control
* Content-Security-Policy
* Referrer-Policy

---

# 📂 Estructura del proyecto

```text
Proyecto/
│
├── main.py
├── README.md
└── Carpeta de reportes/
      ├── Reporte_google.txt
      ├── Reporte_github.txt
      └── ...
```

---

# 📋 Requisitos

* Python 3.10 o superior

Instalar las dependencias con:

```bash
pip install requests rich
```

---

# ▶️ Ejecución

Ejecuta el programa desde la terminal:

```bash
python main.py
```

El programa solicitará las URLs que deseas analizar.

Ejemplo:

```text
Ingrese las direcciones URL:
https://www.google.com https://github.com https://openai.com
```

Las direcciones deben ingresarse **separadas por espacios**.

---

# 📄 Ejemplo de reporte generado

```text
=====================
      REPORTE
=====================

Fecha: 17/07/2026

--------------------------

Content-Type
Cache-Control
Strict-Transport-Security
X-Frame-Options
Referrer-Policy

Encontrados: 5/8
```

---

# ⚙️ Funcionamiento

El programa realiza el siguiente proceso:

1. Solicita al usuario una lista de URLs.
2. Comprueba que cada sitio responda correctamente (códigos HTTP entre 200 y 399).
3. Analiza la presencia de las cabeceras HTTP configuradas.
4. Muestra los resultados en la consola utilizando colores.
5. Genera un archivo de reporte para cada sitio.
6. Guarda todos los reportes dentro de la carpeta **Carpeta de reportes**.

---

# 📚 Librerías utilizadas

* requests
* rich
* pathlib
* shutil
* datetime
* re
* time

---

# 🛡️ Objetivo del proyecto

Este proyecto fue desarrollado con fines educativos para practicar conceptos relacionados con:

* Solicitudes HTTP con la librería Requests.
* Análisis de cabeceras HTTP.
* Seguridad web.
* Manipulación de archivos y directorios.
* Expresiones regulares.
* Uso de barras de progreso con Rich.
* Organización y modularización de código en Python.

---

# 🚀 Posibles mejoras

* Mostrar el valor de cada cabecera encontrada.
* Exportar los reportes a formato PDF.
* Exportar los resultados a Excel o CSV.
* Analizar certificados SSL/TLS.
* Leer las URLs desde un archivo de texto.
* Realizar solicitudes concurrentes para mejorar el rendimiento.
* Generar un resumen general con estadísticas de todos los sitios analizados.

---

# 👨‍💻 Autor

**Angel Kyle Utrilla Solis**

Proyecto desarrollado como práctica del uso de la librería **Requests** para el análisis de cabeceras HTTP relacionadas con la seguridad de aplicaciones web.
