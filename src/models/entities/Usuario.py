from werkzeug.security import check_password_hash
from flask_login import UserMixin
class Usuario(UserMixin):

    def __init__(self,id, nombre, clave,t_usuario="",mail="",is_confirmed=False) -> None:
        self.id=id
        self.nombre=nombre
        self.clave=clave
        self.t_usuario=t_usuario
        self.mail=mail
        self.is_confirmed=is_confirmed

    def to_JSON(self):
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'clave' : self.clave,
            't_usuario' : self.t_usuario,
            'mail' : self.mail,
            'is_auth' : self.is_confirmed
        }
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)