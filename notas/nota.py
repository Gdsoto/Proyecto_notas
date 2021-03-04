import database.conexion as conexion

# acceder al arreglo con la conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Nota:

    def __init__(self, id_usuario, titulo_notas = "", descripcion_nota = ""):
        self.id_usuario = id_usuario
        self.titulo_notas = titulo_notas
        self.descripcion_nota = descripcion_nota

    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.id_usuario, self.titulo_notas, self.descripcion_nota)
        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.id_usuario}"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.id_usuario} AND titulo_notas LIKE '%{self.titulo_notas}%'"
        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]