CONSULTA-ONPE-GARCIA

Descripción
Aplicación en Python que consulta si una persona es miembro de mesa mediante el servicio de la ONPE, utilizando un archivo Excel con DNIs como entrada y generando un archivo con los resultados.

--------------------------------------------------

Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Windows 11
- WSL 2
- Docker (Docker Desktop recomendado)
- Python 3.11 (opcional, solo si se ejecuta fuera de Docker)

Librerías utilizadas:
- selenium
- pandas
- openpyxl
- requests


--------------------------------------------------

Instalación

1. Clonar el repositorio:

git clone https://github.com/Cramess/CONSULTA-ONPE-GARCIA.git
cd CONSULTA-ONPE-GARCIA

2. Verificar que existan los siguientes archivos:

- app.py
- requirements.txt
- dnis.xlsx
- Dockerfile
- Dockerfile.optimizado
- Dockerfile.multistage

--------------------------------------------------

Construcción de imágenes Docker

docker build -t consulta-onpe:base -f Dockerfile .
docker build -t consulta-onpe:optimizado -f Dockerfile.optimizado .
docker build -t consulta-onpe:multistage -f Dockerfile.multistage .

--------------------------------------------------

Ejecución

docker run --rm -it -v %cd%:/app consulta-onpe:base
docker run --rm -it -v %cd%:/app consulta-onpe:optimizado
docker run --rm -it -v %cd%:/app consulta-onpe:multistage

Consideraciones:
- Se solicitará ingresar un token reCAPTCHA manualmente.
- El archivo dnis.xlsx debe estar en la misma carpeta.
- El resultado se generará como resultado.xlsx.

--------------------------------------------------

Comparación de imágenes

Se construyeron tres versiones de la imagen Docker:

- base: configuración básica
- optimizado: incluye mejoras en la instalación de dependencias
- multistage: utiliza construcción por etapas

--------------------------------------------------

Salida

El programa genera:

- resultado.xlsx: contiene los datos consultados de los DNIs

--------------------------------------------------

Autor

Cristian García