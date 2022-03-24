# Clase configurator

class Configurator:
    # Constructor de la clase
    def __init__(self,conf):
        self.conf=conf
        
    def comprobar():
    # Comprobar si existe directorio y archivo de configuracion
        if not os.path.exists("/home/faus/.config/diogenes/"):
            os.mkdir("/home/faus/.config/diogenes/")
            if not os.path.exists(archivo_configuracion):
                datos={}
                datos ["ruta"]="/home/faus/Descargas"
                with open (archivo_configuracion,'w') as file_writer:
                 toml.dump(datos,file_writer)
                 
    def abrir_configuracion():
    # Cargar datos de configuracion
	    with open(archivo_configuracion) as file:
            configuration_file = toml.load(archivo_configuracion)
            return configuration_file