
import shutil
from pathlib import Path


def accion(rutai,rutao,act,filtro):
 
    slice1=slice(1,5)
    filtro=filtro[slice1]
    for archivo in[x for x in rutai.iterdir() if not x.is_dir()]:
        extension=archivo.suffix
        
        if extension==filtro:
            if act=="move":
                shutil.move(archivo,rutao)
            if act=="copy":
                shutil.copy(archivo,rutao)
                    