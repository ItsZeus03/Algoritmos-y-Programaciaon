"""
entradas
kilometros-->float-->ki
salidas
valor_pago-->float-->
"""
ki=float(input("cuantos kilometros recorrio "))
if(ki<=300):
  vl=50000
  print("Total a pagar"+str(vl))
elif(ki>300 and ki<1000):
  vl=70000+(ki-300)*30000
  print("Total a pagar"+str(vl))
elif(ki>=1000):
  vl=150000+(ki-1000)*9000
  print("Total a pagar"+str(vl))  