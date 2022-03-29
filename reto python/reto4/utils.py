# utils.py

# Modulo con funciones 

import mimetypes
from pathlib import Path
import os

# listado de imagenes

def listar_imagenes (ruta_imagenes):
    # Listar archivos de imagenes en carpeta de descargas
    for archivo in[x for x in ruta_imagenes.iterdir() if not x.is_dir()]:
        if not archivo.is_dir() and mimetypes.guess_type(archivo)[0]=='image/jpeg':
            print (archivo)