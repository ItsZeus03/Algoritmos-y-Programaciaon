"""
entradas
invercion-->float-->inv
porcentaje_interes-->float-->pin
dinero_cuenta--.float-->vc
salidas
cantidad_cuenta-->float-->cc
"""
inv=float(input("Ingrese el valor de la invercion "))
pin=float(input("Ingrese el porcentaje de interes "))
vc=float(input("Ingrese el dinero que se encuentra en la cuaneta "))
vin=inv*(pin/100)
if(vin>100000):
  cc=vc
  print("dinero en la cuenta "+str(cc))
else:
  cc=vin+vc
  print("dinero en la cuenta "+str(cc))