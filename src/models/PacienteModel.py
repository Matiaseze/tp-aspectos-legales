from database.db import get_connection
from .entities.Paciente import Paciente

class PacienteModel():

    @classmethod
    def get_pacientes(self):
        try:
            connection=get_connection()
            pacientes=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT numDoc, nombre, apellido, email,telefono,localidad, domicilio FROM pacientes ORDER BY numDoc")
                resultset=cursor.fetchall()
                for row in resultset:
                    paciente=Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                    pacientes.append(paciente.to_JSON())
            
            connection.close()
            return pacientes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_paciente(self, id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT numDoc, nombre, apellido, email,telefono,localidad, domicilio FROM pacientes WHERE numDoc = %s", (id,))
                row=cursor.fetchone()
                paciente = None
                if row is not None:
                    paciente=Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            
            connection.close()
            return paciente
        except Exception as ex:
            raise Exception(ex)