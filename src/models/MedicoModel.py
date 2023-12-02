from database.db import get_connection
from .entities.Medico import Medico

class MedicoModel():

    @classmethod
    def get_medicos(self):
        try:
            connection=get_connection()
            medicos=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, num_doc, nombre, apellido, legajo, mail, telefono, domicilio FROM medicos ORDER BY num_doc")
                resultset=cursor.fetchall()
                for row in resultset:
                    medico=Medico(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    medicos.append(medico.to_JSON())
            
            connection.close()
            return medicos
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_medico(self, id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, num_doc, nombre, apellido,legajo, mail, telefono, domicilio FROM medicos WHERE id = %s",(id,))
                row=cursor.fetchone()
                medico = None
                if row is not None:
                    medico=Medico(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            
            connection.close()

            return medico
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def actualizar_medico(self, id, documento, nombre, apellido,legajo, mail, telefono, domicilio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE medicos SET num_doc= %s, nombre= %s, apellido= %s, legajo= %s, mail= %s, telefono= %s, domicilio=%s WHERE id = %s",
                    (documento, nombre, apellido,legajo, mail, telefono, domicilio, id))

            connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        finally:
            connection.close()