Proceso inicio_salario_neto
	Escribir "Cauntas horas trabajo"
	Leer h
	Escribir "A cuanto le pagan las horas trabajadas"
	Leer vh
	s <- h*vh
	sn <- s-(s*0.2)
	Escribir "Su salario neto es de: " sn
FinProceso
