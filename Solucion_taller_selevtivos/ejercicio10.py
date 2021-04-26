"""
entradas
salario_bruto-->float-->sb
salidas
categoria-->int-->ct
aumento-->int-->aum
salario_neto-->float-->sn
"""
sb=float(input("Ingrese susalario bace "))
if(sb<=9000000):
  sn=sb+(sb*0.6)
  print("categoria 5 aumento del 60% y so salario neto fue de "+str(sn))
elif(sb>9000000 and sb<=2000000):
  sn=sb+(sb*0.4)
  print("categoria 4 aumento del 40% y so salario neto fue de "+str(sn))
elif(sb>2000000 and sb<=3600000):
  sn=sb+(sb*0.2)
  print("categoria 3 aumento del 20% y so salario neto fue de "+str(sn))
elif(sb>3600000 and sb<=4300000):
  sn=sb+(sb*0.15)
  print("categoria 2 aumento del 15% y so salario neto fue de "+str(sn))
else:
  sn=sb+(sb*0.1)
  print("categoria 1 aumento del 10% y so salario neto fue de "+str(sn))