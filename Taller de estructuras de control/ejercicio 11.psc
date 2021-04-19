Proceso inicio_salario
	Escribir "Cuantas horas laboro "
	Leer hl
	Escribir "Cuantas horas extra laboro "
	Leer hex
	Escribir "A cuanto le pagan la hora "
	Leer vh
	Escribir "Cuantos hijos tiene "
	Leer ch
	sb <- hl*vh
	sex <- (vh+(vh*0.25))*hex
	pf <- sb*0.05
	ph <- sb*0.02
	cah <- sb*0.07
	ac <- 250000
	h <- 173000*ch
	prih <- 180000
	as <- ac+h+prih
	de <- pf+ph+cah
	sne <- sb+sex+as-de
	Escribir "las asignacion es de: " as
	Escribir "las deducciones son de: " de
	Escribir "El sueldo neto es de: " sne
FinProceso
