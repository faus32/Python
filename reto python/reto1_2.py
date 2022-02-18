"""
Reto 1

Version 2

Listar solo los archivos de la carpeta descargas del usuario

"""
from gi.repository import GLib 
import os

""" 
Funcion para comprobar si es un archivo o no

Argumentos : vruta1   Recibira el valor del archivo o directorio

Return true si es archivo false si no lo es
"""
def imprimir (vruta1):
    vruta2=ruta_descargas+"/"+vruta1
    if os.path.isfile (vruta2):
        return True
    else: 
        return False



    
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
        varchivo=varchivo.replace ("'"," ")
        tarchivos.append(varchivo.strip())
        varchivo=""
    else:
        varchivo=varchivo+letra
        
# imprimir archivos

for archivo in tarchivos:
    if imprimir(archivo):
        print (archivo)
    
    
       

    