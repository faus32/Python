# reto4 
# Crear clase para gestionar la configuracion
# Crear modulo y importar la funcion de listado de imagenes
from utils import listar_imagenes
import Configurator


def main(app,config):
    configurator=Configurator(config)
    configurator.comprobar
    ruta=configurator.abrir_configuracion
    listar_imagenes(ruta)
    
if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)