# reto4 
# Crear clase para gestionar la configuracion
# Crear modulo y importar la funcion de listado de imagenes

from utils import listar_imagenes
from Configurator import *
from pathlib import Path
from xdg import xdg_config_home

def main(app,config):
    path = Path(xdg_config_home()) / app
    configurator = Configurator(path, config)
    configurator.check_config()
    configurator.read_config()
    
if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)