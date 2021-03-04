import notas.nota as modelo


class Acciones_notas:

    def crear(self, usuario):
        print(f"{usuario[1]} vamos a crear una nota\n")
        titulo = input("Titulo de la nota\n")
        descripcion = input("contenido de la nota\n")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Nota guardada!! titulo: {nota.titulo_notas}")
        else:
            print(f"{usuario[1]}, no se ha podido guardar la nota")

    def mostrar(self, usuario):
        print(f"{usuario[1]} aquí estan tus notas\n")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        print(notas)

        for nota in notas:
            print("\n-----------------------------")
            print(nota[2])
            print(nota[3])
            print("\n-----------------------------")

    def borrar(self, usuario):
        print(f"\n {usuario[1]} vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota a borrar\n")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo_notas}")
        else:
            print("No se ha borrado la nota")