# Clase configurator

import toml
import os

class Configurator():
    def __init__(self,path,config):
        self.path=path
        self.config=config
    
    def check_config (self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            if not os.path.exists(self.path/self.config):
                datos={}
                datos ["ruta"]="/home/faus/Descargas"
                with open (self.path/self.config,'w') as file_writer:
                 toml.dump(datos,file_writer)
            
    def read_config(self):
        print ("leer configuracion")