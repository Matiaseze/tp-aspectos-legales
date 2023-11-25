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
    def get_paciente(self, num_doc):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT num_doc, nombre, apellido, mail, telefono, domicilio FROM pacientes WHERE num_doc = %s",(num_doc,))
                row=cursor.fetchone()
                paciente = None
                if row is not None:
                    paciente=Paciente(row[0],row[1],row[2],row[3],row[4],row[5])
            
            connection.close()
            return paciente
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def actualizar_paciente(self, num_doc, nombre, apellido, mail, telefono, domicilio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE pacientes SET nombre = %s, apellido = %s, mail = %s, telefono = %s, domicilio = %s WHERE num_doc = %s",
                    (nombre, apellido, mail, telefono, domicilio, num_doc))

            connection.commit()
            return True
        except Exception as ex:
            print(f"Error al actualizar paciente: {ex}")
            return False
        finally:
            connection.close()