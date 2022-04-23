# Clase para gestionar la configuracion

import toml
import os
import shutil
from utils import accion
from pathlib import Path

class Configurador():
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
                        "out": "/home/faus/Descargas/imagenesout1",
                        "action":"none"
                    },
                    "directorios2":{
                        "in":"/home/faus/Descargas/imagenesin2",
                        "out":"/home/faus/Descargas/imagenesout2",
                         "action":"move"
                         
                    },
                     "directorios3":{
                        "in":"/home/faus/Descargas/imagenesin3",
                        "out":"/home/faus/Descargas/imagenesout3",
                         "action":"copy"
                         
                    }
                }
                with open (self.path/self.config,'w') as file_writer:
                 toml.dump(datos,file_writer)
                 
    def read_config(self):
        # Cargar datos de configuracion
	    with open(self.path/self.config) as file:
               configuration_file = toml.load(self.path/self.config)
               
               # Comprobar ruta in 1
               vrutai=Path(configuration_file["directorios1"]["in"])
               vrutao=Path(configuration_file["directorios1"]["out"])
               vaccion=configuration_file ["directorios1"]["action"]
               if not os.path.exists(vrutai):
                 os.mkdir(vrutai)  
               # Comprobar ruta out 1 
               if not os.path.exists(vrutao):
                 os.mkdir(vrutao)
               # Comprobar accion
               accion(vrutai,vrutao,vaccion)
               # Comprobar ruta in 2
               vrutai=Path(configuration_file["directorios2"]["in"])
               vrutao=Path(configuration_file["directorios2"]["out"])
               vaccion=configuration_file ["directorios2"]["action"]
               if not os.path.exists(vrutai):
                 os.mkdir(vrutai)
               # Comprobar ruta out 2
               if not os.path.exists(vrutao):
                 os.mkdir(vrutao)
                  # Comprobar accion
               accion(vrutai,vrutao,vaccion)
               
                 
               # Comprobar ruta in 3
               vrutai=Path(configuration_file["directorios3"]["in"])
               vrutao=Path(configuration_file["directorios3"]["out"])
               vaccion=configuration_file ["directorios3"]["action"]
               if not os.path.exists(vrutai):
                 os.mkdir(vrutai)
               # Comprobar ruta out 3
               if not os.path.exists(vrutao):
                 os.mkdir(vrutao)
                # Comprobar accion
               accion(vrutai,vrutao,vaccion)
               
                 
    