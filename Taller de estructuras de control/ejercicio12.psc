Proceso Promedio_general
	Escribir 'Ingrese la calificacion del examen de matematicas '
	Leer exm
	Escribir 'Ingrese las calificaciones de las tres tareas de matematicas '
	Leer tm1
	Leer tm2
	Leer tm3
	Escribir 'Ingrese la calificacion del examen de fisica '
	Leer exf
	Escribir 'Ingrese la calificacion de las tres tareas de fisica '
	Leer tf1
	Leer tf2
	Leer tf3
	Escribir 'Ingrese la calificacion del examen de quimica '
	Leer exq
	Escribir 'Ingrese la calificacion de las tres tares de quimicamn '
	Leer tq1
	Leer tq2
	Leer tg3
	pm <- (exm*0.9)+(((tm1+tm2+tm3)/3)*0.1)
	pf <- (exf*0.8)+(((tf1+tf2+tf3)/3)*0.2)
	pq <- (exq*0.85)+(((tq1+tq2+tq3)/3)*0.15)
	pg<-((pm+pf+pq)/3)
	Escribir "el promedio en matematicas es: " pm
	Escribir "el promedio en fisica es: " pf
	Escribir "el promedio en quimica es: " pq
	Escribir "el promedio en general es: " pg
FinProceso
