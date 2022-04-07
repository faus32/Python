 # Reto5
 # Uso de diccionarios
 
from pathlib import Path
from xdg import xdg_config_home
from Configuracion import *
 
def main(app,config):
    path = Path(xdg_config_home()) / app
    configurador=Configuracion (path,config)
    configurador.check_config()
    configurador.read_config()
 
if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)