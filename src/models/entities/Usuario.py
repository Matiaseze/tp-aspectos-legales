from werkzeug.security import check_password_hash
from flask_login import UserMixin
class Usuario(UserMixin):

    def __init__(self,id, nombre, clave,t_usuario="",mail="") -> None:
        self.id=id
        self.nombre=nombre
        self.clave=clave
        self.t_usuario=t_usuario
        self.mail=mail

    def to_JSON(self):
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'clave' : self.clave,
            't_usuario' : self.t_usuario,
            'mail' : self.mail
        }
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)