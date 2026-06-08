print("Catálogo")
print("1-Genesis 250")
print("2-Xpulse 200")
print("3-CFLITE 230")
cotizador=0
while cotizador <1 or cotizador >3:
    cotizador=int(input("¿Cuál moto desea cotizar? "))
    if cotizador <1 or cotizador >3:
        print("La opción no existe, Intentalo de nuevo")
match cotizador:
    case 1:print("La motocicleta Genesis 250 tiene un costo de: US$2,500.00")
    case 2:print("La motocicleta Xpulse 200 tiene un costo de: US$1,500.00")
    case 3:print("La motocicleta CFLITE 230 tiene un costo de: US$3,300.00")
