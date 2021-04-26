"""
entrada
salariogbace-->float-->sa
salida
salario_neto-->float-->sn
"""
sa=float(input("Ingrese su salario bace "))
if(sa>900000):
  sn=sa+(sa*0.12)
  print("Su salario es de "+str(sn))
else:
  sn=sa+(sa*0.15)
  print("Su salario es de "+str(sn))  