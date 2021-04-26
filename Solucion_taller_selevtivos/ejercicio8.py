"""
entradas
valor_p-->int-->P
valor_q-->int-->Q
salidas
valores-->str
"""
P=int(input("Ingrese el valor de P "))
Q=int(input("Ingrese el valor de Q "))
n=P**3+Q**4-2*P**2
if(n>680):
  print(str(P)+" y "+str(Q)+" Satisfacen la exprecion")
else:
  print(str(P)+" y "+str(Q)+" No Satisfacen la exprecion") 