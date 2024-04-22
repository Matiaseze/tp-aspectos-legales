from database.db import get_connection
from .entities.Paciente import Paciente

class PacienteModel():

    @classmethod
    def get_pacientes(self):
        try:
            connection=get_connection()
            pacientes=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT num_doc, nombre, apellido, mail, telefono, domicilio FROM pacientes ORDER BY num_doc")
                resultset=cursor.fetchall()
                for row in resultset:
                    paciente=Paciente(row[0],row[1],row[2],row[3],row[4],row[5])
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
                cursor.execute("SELECT id, num_doc, nombre, apellido, mail, telefono, domicilio FROM pacientes WHERE id = %s",(id,))
                row=cursor.fetchone()
                paciente = None
                if row is not None:
                    paciente=Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            
            connection.close()
            return paciente
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def actualizar_paciente(self, id, documento, nombre, apellido, mail, telefono, domicilio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE pacientes SET num_doc= %s, nombre= %s, apellido= %s, mail= %s, telefono= %s, domicilio=%s WHERE id = %s",
                    (documento, nombre, apellido, mail, telefono, domicilio, id))

            connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        finally:
            connection.close()