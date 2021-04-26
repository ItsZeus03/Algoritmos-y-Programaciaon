"""
entradas
valorA-->float-->A
valorB-->float-->B
valorC-->float-->C
salidas
valor_cuacion-->float-->va
"""
A=float(input("Ingrese el valor de A "))
B=float(input("Ingrese el valor de B "))
C=float(input("Ingrese el valor de C "))
D=B**2-4*A*C
if(D==0):
  X1=X2=-B/(2*A)
  print("El valor de x1 es "+str(X1)+" y el valor de x2 es "+str(X2))
elif(D>0):
  X1=(-B+(B**2-4*A*C)**0.5)/(2*A)
  X2=(-B-(B**2-4*A*C)**0.5)/(2*A)
  print("El valor de x1 es "+str(X1)+" y el valor de x2 es "+str(X2))
else:
  print("no tiene solución en los Reales.")