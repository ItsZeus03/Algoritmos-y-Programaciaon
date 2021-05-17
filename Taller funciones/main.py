frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
elemento-->str-->elemento

Salidas
lista-->lista_frutas
"""
def eliminar_un_caracter(lista,elemento):
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar
pass
#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
lista-->lista
Salidas
lista-->lista
"""
def copia_lista(lista):
  aux=[]
  for i in lista:
    aux.append(i) 
  return lista.copy() 
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-->lista
Salidas
lista-->lista
"""  
def numeros_pares(lista):
  aux=[]
  for i in (lista):
    if(float(i)%2==0):
      aux.append(i)
  return aux    
  pass#RetornaUnaLista
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-->lista
elemento-->str-->elemento
Salidas
lista-->lista
"""  
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista
  pass#RetornaUnaLista 

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
Salidas
"""  
def letra(lista,elemento):
  aux=[]
  b=str(input(" "))
  for i in lista:
    a=i.replace(elemento,b)
    aux.append(a)
  return aux  
  pass  
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista-->list-->lista
Salidas
tamaño-->int-->tamaño
"""   
def tamano_lista(lista):
  aux=[]
  tama=0
  for i in lista:
    tama=tama+1 
  aux.append(tama)  
  return aux  
  pass #RetornaUnEntero
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista
"""  
def informacion_lista(lista):
  aux=[]
  tama=0
  for i in lista:
    tama=tama+1 
  aux.append(tama)
  print(type(aux))
  return aux 
  pass
#Retornar una lista con los numero negativos  
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista
"""   
def numeros_negativos(lista):
  aux=[]
  for i in (lista):
    i=int(i)
    if(i<0):
      aux.append(i)  
  return aux
  pass
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
def posicion_elemento(lista):
  c=0
 for i in lista:
   lista.append(i)
   a=" ".join(lista)
   c=c+1 
   if(a=="Fresa"):
     print(c)
     break
  return lista   
  pass
"""
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(lista):
  aux=[]
  for i in lista:
    aux.append(i)  
  valor=str(input("Ingrese valor:"))
  aux.append(valor)
  return aux
  pass
#Realizar una funcion que cuente el numero de veces que se repite un elemento  
def repetir(lista):
  aux=[]
  contador=0
  valor=str(input("ingrese dato "))
  for i in lista:
    if(i==valor):
      contador=contador+1
    else:
      contador=contador
  aux.append(contador)    
  return aux
  pass
  
if __name__ == "__main__":
  nueva=repetir(lista_frutas)
  print(nueva) 
