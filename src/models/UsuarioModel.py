from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel():

    @classmethod
    def login(self, user):
        try:

            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, usuario, clave, t_usuario, mail, is_confirmed FROM usuarios WHERE usuario = %s", (user.usuario,))
                row=cursor.fetchone()
                usuario = None
                if row is not None:
                    usuario=Usuario(row[0],row[1],Usuario.check_password(row[2], user.clave),row[3],row[4],row[5])
                    return usuario
            connection.close()
            print('DEBUG: login')
            print(usuario.is_confirmed)
            return usuario
        except Exception as ex:

            raise Exception(ex)

    @classmethod
    def user_confirmed(self, user):       

        print('DEBUG: login')
        print(user.is_confirmed)

        if user.is_confirmed:
            return ('La cuenta ya ha sido confirmada. Inicia sesión.')
        else:
            try:
                connection = get_connection()

                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE usuarios SET is_confirmed=True WHERE id = %s",
                        (user.id,))
                print('Usuario confirmado?')    
                print(user.is_confirmed)
                print(user.usuario)
                connection.commit()
                return ('Has confirmado tu cuenta. Gracias.')
            except Exception as ex:
                raise Exception(ex)
            finally:
                connection.close()
            

    @classmethod
    def get_usuarios(self):
        try:
            connection=get_connection()
            usuarios=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, usuario, t_usuario, mail FROM usuarios ORDER BY id")
                resultset=cursor.fetchall()
                for row in resultset:
                    usuario=Usuario(row[0],row[1],row[2],row[3],row[4])
                    usuarios.append(usuario.to_JSON())
            
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_usuario_id(self, id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, usuario, t_usuario, mail, is_confirmed FROM usuarios WHERE id = %s", (id,))
                row=cursor.fetchone()
                usuario = None
                if row is not None:
                    usuario=Usuario(row[0],row[1],0,t_usuario=row[2],mail=row[3],is_confirmed=row[4])
            
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_usuario_mail(self, email):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, usuario, t_usuario, mail, is_confirmed FROM usuarios WHERE mail = %s", (email,))
                row=cursor.fetchone()
                usuario = None
                if row is not None:
                    usuario=Usuario(row[0],row[1],0,t_usuario=row[2],mail=row[3],is_confirmed=row[4])
                    print('DEBUG: get_usuario_mail 1')
                    print(usuario.id)
                    print(usuario.usuario)
                    print(usuario.clave)
                    print(usuario.is_confirmed)
            
            connection.close()

            print('DEBUG: get_usuario_mail 2')
            print(usuario.is_confirmed)
            return usuario
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_tipo_usuario(cls, username):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT t_usuario FROM usuarios WHERE usuario = %s", (username,))
                tipo_usuario = cursor.fetchone()
            connection.close()
            return tipo_usuario[0] if tipo_usuario else None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_usuario(self, usuario):
        clave = Usuario.generate_password(usuario.clave)

        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO usuarios (id, usuario, clave, mail, t_usuario, is_confirmed) VALUES ((SELECT COUNT(id)+1 FROM usuarios),%s, %s, %s, %s, %s)", 
                               (usuario.usuario, clave, usuario.mail, usuario.t_usuario, usuario.is_confirmed))
                connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        finally:
            connection.close()
        