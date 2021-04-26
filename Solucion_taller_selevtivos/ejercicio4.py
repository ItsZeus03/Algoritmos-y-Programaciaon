"""
emtradas
valor_total_compra-->float-->vtc
salida
fondos_empresa-->flaot-->fp
credito-->float-->cr
interes-->float-->inter
prestamo_banco-->float-->pb
"""
vtc=float(input("Ingres el valo total de la compra "))
if(vtc>5000000):
  fp=vtc*0.55
  cr=vtc*0.15
  inte=cr*0.2
  pb=vtc*0.15
  print("Cantidad invertida por la empresa "+str(fp))
  print("Cantidad pagada a credito "+str(cr))
  print("Cantidad pagada por el interes "+str(inte))
  print("Cantidad del prestamo al banco "+str(pb))
else:
  fp=vtc*0.70
  cr=vtc*0.2
  inte=cr*0.2
  print("Cantidad invertida por la empresa "+str(fp))
  print("Cantidad pagada a credito "+str(cr))
  print("Cantidad pagada por el interes "+str(inte))