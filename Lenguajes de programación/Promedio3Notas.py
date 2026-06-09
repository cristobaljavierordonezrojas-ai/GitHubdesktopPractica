contador=1
nota=0
while contador<=3:
    if contador==1:
        notas=float(input("Ingresa Una nota Optenida "))
    else:
        notas=float(input("Ingresa Otra nota Optenida "))
    nota=nota+notas
    contador=contador+1
promedio=nota/(contador-1)
print(f"Su promedio de calificaciones es de: {promedio:.2f}")
