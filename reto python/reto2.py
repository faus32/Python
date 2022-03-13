# Reto2
# Listar todos los archivos de imagenes (jpg,jpeg,JPEG)
#
# Si en el nombre del archivo aparece un numero se visualizara el nombre en mayuscula
# Si es par poner delante el simbolo =>

# Guardar directorio de descargas del usuario

from pathlib import Path

from gi.repository import GLib 


directorio = Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))

if directorio.is_dir():
            contador=0
            for archivo in[x for x in directorio.iterdir() if not x.is_dir()]:
 # comprobar extension
                
                extension=archivo.suffix
                if extension==".jpg" or extension==".jpeg" or extension==".JPEG":    
                    contador+=1
                    nombre=archivo.name
                    imprimir=str(nombre)
# Comprobar numero en nombre de archivo                   
                    if any(chr.isdigit() for chr in nombre):
                        imprimir=imprimir.upper()
                    if contador % 2==0:
                        imprimir="=>"+imprimir
                    print (imprimir)
               


