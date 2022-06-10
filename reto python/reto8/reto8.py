 # Reto 8
 # Tedimensionar imagenes
 
 
from pathlib import Path
from PIL import Image

class Redimensionar:
    
    def __init__ (self,filein,fileout,args):
        self.__filein=filein
        self.__fileout=fileout
        self.__args=args
    
    def check(self):
        
        if not self.__filein.exists() or not self.__filein.is_file():
            return False
        return True

        
    def execute (self):
       
        imagen=Image.open (self.__filein)
        imagen2=imagen.resize((self.__args["ancho"],self.__args["alto"]))
        imagen2.save (self.__fileout)
        print ("Imagen Redimensionada")
    


def main(app,config):
    filein = Path("/home/faus/Descargas/python/imagen1.png")
    fileout= Path("/home/faus/Descargas/python/imagen2.png")
    args={"ancho":200,"alto":200}
    redimensionar=Redimensionar (filein,fileout,args)
    if redimensionar.check():
        redimensionar.execute()
   
    
 
if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)