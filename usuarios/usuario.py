import database.conexion as conexion
import datetime
import hashlib

#acceder al arreglo con la conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

#Creacion de clase Usuario
class Usuario:
    #Constructor
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    
    #Metodo registrar
    def registrar(self):
        fecha = datetime.datetime.now()
        #cifrado de contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))

        sql = "INSERT INTO usuarios VALUES(null,%s, %s, %s, %s,%s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
    
    #Metodo Login
    def identificar(self):
        return self.nombre
