"""
entradas
ventas_departament1-->int-->vd1
ventas_departament2-->int-->vd2
ventas_departament3-->int-->vd3
sueldo_bace-->float-->sb
salidas
salario_final-->float-->sf
"""
vd1=int(input("Ingrese las ventas del departamento 1 "))
vd2=int(input("Ingrese las ventas del departamento 2 "))
vd3=int(input("Ingrese las ventas del departamento 3 "))
sb=float(input("Ingrese el salario bace "))
tv=vd1+vd2+vd3
if(vd1>(tv*0.33)):
  sf=sb+(sb*0.2)
  print("el salario final para el departamento 1 es de "+str(sf))
else:
  print("el salario final para el departamento 1 es de "+str(sb))
if(vd2>(tv*0.33)):
  sf=sb+(sb*0.2)
  print("el salario final para el departamento 2 es de "+str(sf))
else:
   print("el salario final para el departamento 2 es de "+str(sb))
if(vd3>(tv*0.33)):
  sf=sb+(sb*0.2)
  print("el salario final para el departamento 3 es de "+str(sf))
else:
   print("el salario final para el departamento 3 es de "+str(sb))