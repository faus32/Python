 # Reto6
 # Manejo de archivos
 
from pathlib import Path
from xdg import xdg_config_home
from Configurador import *

def main(app,config):
    vpath = Path(xdg_config_home()) / app
    configurar= Configurador (vpath,config)
    configurar.check_config()
    configurar.read_config()
 
if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)