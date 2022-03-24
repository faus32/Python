# reto3


# Crear archivo configuración.
# Si archivo no existe crearlo y si existe cargar el directorio por defecto y visualizar imagenes

# Usando toml-0.10.2 para gestionar la configuracion
# Usado mimetypes para filtrar imagenes

import toml
import mimetypes
import os
from pathlib import Path

def comprobar():
    # Comprobar si existe directorio y archivo de configuracion
    if not os.path.exists("/home/faus/.config/diogenes/"):
        os.mkdir("/home/faus/.config/diogenes/")
        if not os.path.exists(archivo_configuracion):
            datos={}
            datos ["ruta"]="/home/faus/Descargas"
            with open (archivo_configuracion,'w') as file_writer:
             toml.dump(datos,file_writer)
        
def abrir_configuracion():
    # Cargar datos de configuracion
	 with open(archivo_configuracion) as file:
            configuration_file = toml.load(archivo_configuracion)
            return configuration_file

def listar_imagenes (ruta_imagenes):
    for archivo in[x for x in ruta_imagenes.iterdir() if not x.is_dir()]:
        if not archivo.is_dir() and mimetypes.guess_type(archivo)[0]=='image/jpeg':
            print (archivo)

# Comienzo de la aplicacion{}

archivo_configuracion="/home/faus/.config/diogenes/diogenes.conf"
comprobar()
configuracion=abrir_configuracion()
vruta=configuracion['ruta']
listar_imagenes (Path(vruta))
