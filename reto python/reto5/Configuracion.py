# Clase para gestionar la configuracion

import toml
import os
from pathlib import Path

class Configuracion():
    def __init__(self,path,config):
        self.path=path
        self.config=config
        
# Comprobar si existe la carpeta y el archivo de configuracion
        
    def check_config (self):
        # Comprobar si existen el directorio y el archivo de configuracion
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            if not os.path.exists(self.path/self.config):
                datos= {
                    
                    "directorios1":{
                        "in":"/home/faus/Descargas/imagenesin1",
                        "out": "/home/faus/Descargas/imagenesout1"
                    },
                    "directorios2":{
                        "in":"/home/faus/Descargas/imagenesin2",
                        "out":"/home/faus/Descargas/imagenesout2" 
                     }
                }
                
                with open (self.path/self.config,'w') as file_writer:
                 toml.dump(datos,file_writer)
                 
    def read_config(self):
        # Cargar datos de configuracion
	    with open(self.path/self.config) as file:
               configuration_file = toml.load(self.path/self.config)
               # Comprobar ruta in 1
               vruta=Path(configuration_file["directorios1"]["in"])
               if not os.path.exists(vruta):
                 os.mkdir(vruta)  
               # Comprobar ruta out 1 
               vruta=Path(configuration_file["directorios1"]["out"])
               if not os.path.exists(vruta):
                 os.mkdir(vruta)
               # Comprobar ruta in 2
               vruta=Path(configuration_file["directorios2"]["in"])
               if not os.path.exists(vruta):
                 os.mkdir(vruta)
               # Comprobar ruta out 2
               vruta=Path(configuration_file["directorios2"]["out"])
               if not os.path.exists(vruta):
                 os.mkdir(vruta)
                 
               
            