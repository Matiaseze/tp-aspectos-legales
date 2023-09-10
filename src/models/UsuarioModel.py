from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel():

    @classmethod
    def login(self, user):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, clave, t_usuario, mail FROM usuarios WHERE nombre = %s", (user.nombre,))
                row=cursor.fetchone()
                usuario = None
                if row is not None:
                    usuario=Usuario(row[0],row[1],Usuario.check_password(row[2], user.clave),row[3],row[4])
                    return usuario
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_usuarios(self):
        try:
            connection=get_connection()
            usuarios=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, t_usuario, mail FROM usuarios ORDER BY id")
                resultset=cursor.fetchall()
                for row in resultset:
                    usuario=Usuario(row[0],row[1],row[2],row[3],row[4])
                    usuarios.append(usuario.to_JSON())
            
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_usuario(self, id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, t_usuario, mail FROM usuarios WHERE id = %s", (id,))
                row=cursor.fetchone()
                usuario = None
                if row is not None:
                    usuario=Usuario(row[0],row[1],row[2],row[3])
            
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)