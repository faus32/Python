# prueba con modulo os

import os
from typing import runtime_checkable

ruta="/home/faus/Descargas"
archivos=os.listdir(ruta)

# print (os,os.listdir(ruta))


tarchivos=[]
varchivo=""
for letra in archivos:
    if (letra==","):
        # añadir archivo a la lista
        print (varchivo)
        tarchivos.append(varchivo)
        varchivo=""
    else:
        varchivo=varchivo+letra
    
# Visualizar archivos
for i in tarchivos:
    print (i)
