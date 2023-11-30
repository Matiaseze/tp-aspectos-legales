from flask_login import UserMixin
class Medico(UserMixin):

    def __init__(self,id, numDoc, nombre, apellido,legajo, email,telefono, domicilio) -> None:
        self.id=id
        self.numDoc=numDoc
        self.nombre=nombre
        self.apellido=apellido
        self.legajo=legajo
        self.email=email
        self.telefono=telefono
        self.domicilio=domicilio

    def to_JSON(self):
        return {
            'id' : self.id,
            'numDoc' : self.numDoc,
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'legajo' : self.legajo,
            'email' : self.email,
            'telefono' : self.telefono,
            'domicilio' : self.domicilio
        }