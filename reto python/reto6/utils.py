
import shutil
from pathlib import Path


def accion(rutai,rutao,act):
 
    for archivo in[x for x in rutai.iterdir() if not x.is_dir()]:
        if act=="move":
            shutil.move(archivo,rutao)
        if act=="copy":
            shutil.copy(archivo,rutao)
                    