from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
class Usuario(UserMixin):

    def __init__(self,id, usuario, clave,t_usuario="",mail="",is_confirmed="") -> None:
        self.id=id
        self.usuario=usuario
        self.clave=clave
        self.t_usuario=t_usuario
        self.mail=mail
        self.is_confirmed=is_confirmed

    def to_JSON(self):
        return {
            'id' : self.id,
            'usuario' : self.usuario,
            'clave' : self.clave,
            't_usuario' : self.t_usuario,
            'mail' : self.mail,
            'is_confirmed' : self.is_confirmed
        }
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    @classmethod
    def generate_password(self, password):
        return generate_password_hash(password)