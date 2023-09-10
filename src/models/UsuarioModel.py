from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel():
    @classmethod
    def get_usuario(self):
        try:
            connection=get_connection()
            usuarios=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_usuario, nombre, clave, t_usuario, mail FROM usuarios ORDER BY id_usuario")
                resultset=cursor.fetchall()

                for row in resultset:
                    usuario=Usuario(row[0],row[1],row[2],row[3],row[4])
                    usuarios.append(usuario)
            
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)