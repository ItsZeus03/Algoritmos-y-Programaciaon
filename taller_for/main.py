archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M 
"""" 
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="U"):
    print(i) 
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
contador=0
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    contador=contador+1
    lista.append(i[r])
  a="".join(lista)
  print(a)
  print(contador)
  lista=[]
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    if(r=="Singapur")
     lista.append(i[r])
     break
  a="".join(lista)
  print(a)
  lista=[]
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i=="Venezuela"):
    print("Venezuela: Caracas")
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
contador=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    contador=contador+1
    lista.append(i[r])
  a="".join(lista)
  print(a)
  print(contador)
  lista=[]
"""  
#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i=="Bogota"):
    print(i)
"""
#imprima la posicion del pais de Uganda
"""
contador=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  ccontador=ccontador+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
""""
contador=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  ccontador=ccontador+1 
  if(a=="México: Ciudad de México\n"):
    break
  lista=[]   
print(c)
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato

#Agregue un país que no esté en la lista 

archivo.clo