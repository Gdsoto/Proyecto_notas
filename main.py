#importando clase acciones
from usuarios import acciones

print("""
Acciones Disponibles:
    - Registro o login.
""")

funcion = acciones.Acciones()
accion = input("Que quieres hacer?\n")

if accion == "Registro":
    funcion.registro()
elif accion == "Login":
    funcion.login()
