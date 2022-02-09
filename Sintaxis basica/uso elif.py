# Uso de elif

print ("Evaluacion de notas")

nota=int(input("Nota del alumno :"))

if nota<5:
  print ("Insuficiente")
elif nota <6:
  print ("Suficiente") 
elif nota<7:
  print ("Bien") 
elif nota <9:
  print ("Notable") 
else:
  print ("Sobresaliente") 