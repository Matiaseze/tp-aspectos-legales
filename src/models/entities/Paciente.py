from flask_login import UserMixin
class Paciente(UserMixin):

    def __init__(self,numDoc, nombre, apellido, email,telefono, domicilio) -> None:
        self.numDoc=numDoc
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.telefono=telefono
        self.domicilio=domicilio

    def to_JSON(self):
        return {
            'numDoc' : self.numDoc,
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'email' : self.email,
            'telefono' : self.telefono,
            'domicilio' : self.domicilio
        }