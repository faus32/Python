# Condicionales

print ("Evaluación de notas") 
notalaumno=input("Nota del alumno:" ) 
print (evaluacion(int(notaalumno)) ) 

#Funciones

def evaluacion (nota) :
    valoracion ="Aprobado"
    if nota<5:
      valoracion="suspenso"
    return valoracion
  

