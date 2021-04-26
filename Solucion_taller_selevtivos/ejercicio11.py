"""
entradas
temperatura-->float-->t
salida
deporte-->str-->d
"""
t=float(input("Digite la temperatura "))
if(t>85):
  print("Natacion")
elif(t>70 and t<=85):
  print("tenis")
elif(t>33 and t<=70):
  print("gloft")
elif(t>10 and t<=32):
  print("Esqui") 
elif(t<=10):
  print("Marcha")
else:
  print("No se reconoce el deporte ")  