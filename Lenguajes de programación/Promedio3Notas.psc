Algoritmo Promedio
	Definir nota, contador, notas como entero;
	Definir prom Como Real;
	contador<-0;
	notas<-0;
	Mientras contador<3 Hacer
		Si contador=0 Entonces
			Escribir "Ingresa una Nota Optenida"
			Leer nota;
		SiNo
			Escribir "Ingresa otra Nota Optenida"
			Leer nota;
		Fin Si
		contador<-contador+1
		notas<- notas+nota;
	Fin Mientras
	prom <-notas/contador;
	Escribir "Su Promedio de calificaciones es de: ",prom;
FinAlgoritmo
