"""
entradas
edad-->int-->ed
hemoglovina-->float-->hm
salidas
resultado-->str
"""
ed=int(input("ingrese su edad en meses "))
hm=float(input("Ingrese su nivel de hemoglobina en % "))
if(ed>=0 and ed<=1):
  if(hm>=12 and hm<=26):
    print("Negativo de anemia")
  else:
    print("positivo de anemia")
elif(ed>1 and ed<=6):
  if(hm>=10 and hm<=18):
    print("Negativo de anemia")
  else:
    print("positivo de anemia")
elif(ed>6 and ed<=12):
  if(hm>=11 and hm<=15):
    print("Negativo de anemia")
  else:
    print("positivo de anemia")
elif(ed>12 and ed<=60):
  if(hm>=11.5 and hm<=15):
    print("Negativo de anemia")
  else:
    print("positivo de anemia")
elif(ed>60 and ed<=120):
  if(hm>=12.6 and hm<=15.5):
    print("Negativo de anemia")
  else:
    print("positivo de anemia")
elif(ed>120 and ed<=180):
  if(hm>=13 and hm<=15.5):
    print("Negativo de anemia")
  else:
    print("positivo de anemia")