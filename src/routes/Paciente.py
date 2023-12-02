from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
from flask_login import current_user
#Modelos
from models.PacienteModel import PacienteModel


main=Blueprint('paciente_blueprint',__name__)


@main.route('/')
def get_pacientes():
    try:
        pacientes=PacienteModel.get_pacientes()
        return jsonify(pacientes)
    except Exception as ex:
        return jsonify({'message' : str(ex)}),500
    
@main.route('/<id>')
def get_paciente(id):
    try:
        paciente=PacienteModel.get_paciente(id)
        if paciente is not None:
            return jsonify(paciente)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message' : str(ex)}),500
    
@main.route('/info')
def ver_info_paciente():
    try:
        id = current_user.id
        
        paciente = PacienteModel.get_paciente(id)
        
        if paciente is not None:
            return render_template('pacientes/mi_info.html', paciente=paciente)
        else:
            flash('Paciente no encontrado', 'danger')

    except Exception as ex:

        flash('Error al obtener la información del paciente', 'danger')
        return redirect(url_for('home'))
    
@main.route('/<id>/modificar', methods=['GET', 'POST'])

def modificar_paciente(id):
    if request.method == 'GET':
        try:

            paciente = PacienteModel.get_paciente(id)

            if paciente is not None:

                return render_template('pacientes/modificar_paciente.html', paciente=paciente)
            else:
                flash('Paciente no encontrado', 'danger')
                return redirect(url_for('home'))
        except Exception as ex:

            flash('Error al obtener la información del paciente', 'danger')
            return redirect(url_for('home'))
    elif request.method == 'POST':

        try:
            # Recuperar datos del formulario
            documento = request.form.get('documento')
            nombre = request.form.get('nombre')
            apellido = request.form.get('apellido')
            email = request.form.get('email')
            telefono = request.form.get('telefono')
            domicilio = request.form.get('domicilio')
  
            if PacienteModel.actualizar_paciente(id, documento, nombre, apellido, email, telefono, domicilio):
                flash('Información del paciente actualizada correctamente', 'success')
            else:
                flash('Error al actualizar la información del paciente', 'danger')

            return redirect(url_for('home'))
        except Exception as ex:

            flash('Error al actualizar la información del paciente', 'danger')
            return redirect(url_for('home'))
