import math
"""
entradas
varable_A-->float-->a
varable_B-->float-->b
varable_C-->float-->c
varable_D-->float-->d
salidas
resultado_operacion-->float-->ro
"""
a=float(input("Ingrese el valor de A "))
b=float(input("Ingrese el valor de B "))
c=float(input("Ingrese el valor de C "))
d=float(input("Ingrese el valor de D "))
if(d==0):
  ro=(a-c)**2
  print("El resultado es "+str(ro))
elif(d>0):
  ro=(a-b)**3 
  print("El resultado es "+str(ro))
else:
  print("No se puede calcular el resultaado")