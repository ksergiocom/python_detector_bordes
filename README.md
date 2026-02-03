# Detector de Bordes por Gradiente

Este proyecto implementa un detector de bordes básico basado en gradiente en Python. Permite detectar los bordes de una imagen en escala de grises y generar imágenes binarias con distintos valores de umbral.

## Requisitos

`Python 3.8 o superior`

## Librerías:

- numpy
- pillow
- matplotlib

## Instalación

Crear un entorno virtual:

`python3 -m venv venv`

Activar el entorno virtual:

`source venv/bin/activate`

Instalar las dependencias:

`pip install numpy pillow matplotlib`

## Uso

Colocar la imagen que se quiere procesar en el directorio del proyecto. Por defecto se usa cameraman.png.

Ejecutar el script:

`python detector_bordes.py`

El script genera:

- **original_y_gradiente.png:** imagen original y magnitud del gradiente.
- **umbrales_varios.png:** imágenes de bordes con distintos valores de umbral.
