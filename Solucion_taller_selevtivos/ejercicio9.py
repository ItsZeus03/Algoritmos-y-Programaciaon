"""
entradas
nombre-->str-->n
valor_compra-->float-->vc
salidas
total_pago-->float-->tp
"""
n=str(input("Ingrese su nombre "))
vc=float(input("Ingrese el valor de la compra "))
if(vc<50000):
  print(n+" Su total a pagar "+str(vc)+" sin descuento ")
elif(vc>=50000 and vc<100000):
  tp=vc-(vc*0.05)
  print(n+" Su total a pagar "+str(vc)+" sin descuento")
elif(vc>=100000 and vc<700000):
  tp=vc-(vc*0.11)
  print(n+" Su total a pagar "+str(vc)+" sin descuento")
elif(vc>=700000 and vc<1500000):
  tp=vc-(vc*0.18)
  print(n+" Su total a pagar "+str(vc)+" sin descuento")
else:
  tp=vc-(vc*0.25)
  print(n+" Su total a pagar "+str(vc)+" sin descuento")
  