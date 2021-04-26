"""
entradas
lectura_antigua-->float-->lan
lectura_actual-->float-->lac
salida
pago-->float-->pa
"""
fa=input("Ingrese los klivatios consumidos en el mes pasado y el actual (mespasado mesactual) ")
(lan,lac)=fa.split(" ")
lan=float(lan)
lac=float(lac)
kv=lac-lan
if(kv>=0 and kv<=100):
  pa=kv*4600
  print("Total a pagar "+str(pa)+" COP")
elif(kv>=101 and kv<=300):
  pa=kv*8000
  print("Total a pagar "+str(pa)+" COP")
elif(kv>=301 and kv<=500):
  pa=kv*100000
  print("Total a pagar "+str(pa)+" COP")
else:
  pa=kv*120000
  print("Total a pagar "+str(pa)+" COP")