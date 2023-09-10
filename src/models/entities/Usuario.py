class Usuario():

    def __init__(self,id_usuario, nombre=None, clave=None,t_usuario=None,mail=None) -> None:
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.clave=clave
        self.t_usuario=t_usuario
        self.mail=mail

def to_JSON(self):
    return {
        'id_usuario' : self.id_usuario,
        'nombre' : self.id_usuario,
        'clave' : self.clave,
        't_usuario' : self.t_usuario,
        'mail' : self.mail
    }