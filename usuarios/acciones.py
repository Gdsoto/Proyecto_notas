import usuarios.usuario as modelo
import notas.acciones_notas

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

        try:
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]} te has registrado el {login[5]}\n")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))   
            print(type(e).__name__)   
            print("Login incorrecto")
    
    def proximasAcciones(self, usuario):
        print("""
        Acciones Disponibles
            - Crear Nota (crear)
            - Mostrar Notas (mostrar)
            - Eliminar Notas (eliminar)
            - Salir (salir)
        """)
    
        accion = input("Que quieres hacer?\n")
        funcion = notas.acciones_notas.Acciones_notas()

        if accion == 'crear':
            funcion.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'mostrar':
            funcion.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'eliminar':
            funcion.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'salir':
            print(f"{usuario[1]}  hasta pronto!!\n")
            exit()

        return None