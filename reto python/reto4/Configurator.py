# Clase configurator

import toml
import os
from pathlib import Path

class Configurator():
    def __init__(self,path,config):
        self.path=path
        self.config=config
    
    def check_config (self):
        # Comprobar si existen el directorio y el archivo de configuracion
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            if not os.path.exists(self.path/self.config):
                datos={}
                datos ["ruta"]="/home/faus/Descargas"
                with open (self.path/self.config,'w') as file_writer:
                 toml.dump(datos,file_writer)
            
    def read_config(self):
        # Cargar datos de configuracion
	    with open(self.path/self.config) as file:
               configuration_file = toml.load(self.path/self.config)
               return (Path(configuration_file['ruta']))