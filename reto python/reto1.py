# Reto 1
# Listar solo los archivos de la carpeta de descargas

"""
Reto 1

Listar solo los archivos de la carpeta descargas del usuario

"""
from gi.repository import GLib 
import os

# Obtener ruta de descargas del usuario

ruta_descargas=GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD)
print ("Directorio: "+ruta_descargas+"\n")

# Obtener contenido de la carpeta de descargas

contenido=str(os.listdir(ruta_descargas))


# Separar nombres de archivos 
tarchivos=[]
varchivo=""

for letra in contenido:
    if letra==",":
        # añadir archivo a la lista
        tarchivos.append(varchivo.strip())
        varchivo=""
    else:
        if letra !="'":
            varchivo=varchivo+letra
            

    
for archivo in tarchivos:
    vruta=ruta_descargas+"/"+archivo
    if os.path.isfile(vruta):
       print (archivo)