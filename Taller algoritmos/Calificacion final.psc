Proceso Inicio_Calificaciones
	Escribir "ingrese la calificacion de sus parciales"
	Leer p1
	Leer p2
	Leer p3
	Escribir "ingrese la calificacion de su examen final"
	Leer ef
	Escribir "ingrese la calificacion de su trabajo final"
	Leer tf
	a<-((p1+p2+p3)/3)*0.55
	b<-ef*0.3
	c<-tf*0.15
	ct<-a+b+c
	Escribir "Su calificacion final es " ct
FinProceso
