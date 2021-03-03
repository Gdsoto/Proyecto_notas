import usuarios.usuario as modelo

# Creacion de clase Acciones
class Acciones:

    # Funcion registro:
    # solicita los datos de registro al usuario

    def registro(self):
        print("Ok vamos a registrarte...\n")

        nombre = input("Cual es tu nombre?\n")
        apellido = input("Cual es tu apellido?\n")
        email = input("Cual es tu email?\n")
        password = input("Crea una password\n")

        usuario = modelo.Usuario(nombre,apellido,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Bien, {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("Error en el registro")

    # Funcion login:
    # solicita los datos de login al usuario

    def login(self):
        print("Bien!! Identificate en el sistema")

        email = input("Cual es tu email?\n")
        password = input("escribe la contraseña\n")
