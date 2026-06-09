user="admin"
password="SQL2026"
usuario=""
contraseña=""
while user!=usuario or password!=contraseña:
  usuario=input("Usuario: ")
  contraseña=input("Contraseña: ")
  if user!=usuario:
    print("El Usuario no Exciste, Intentalo de Nuevo")
  elif password!=contraseña:
    print("Clave Incorrecta, Intentalo de Nuevo")
  else:
    print("Acceso Concedido, Bienvenido")
  