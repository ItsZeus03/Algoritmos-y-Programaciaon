Proceso Inicio_Convercion_Tiempo
	Escribir "Diguite el tiempo en min"
	Leer t
	min<-t%60
	h1<-t-min
	h<-h1/60
	Escribir "han transcurrido " h " horas y " min " minutos"
FinProceso
