from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for

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
    
@main.route('/<num_doc>/info')
def ver_info_paciente(num_doc):
    try:
        paciente = PacienteModel.get_paciente(num_doc)
        print(paciente)
        if paciente is not None:
            return render_template('info_paciente.html', paciente=paciente)
        else:
            flash('Paciente no encontrado', 'danger')
            return redirect(url_for('paciente_blueprint.get_pacientes'))
    except Exception as ex:
        flash('Error al obtener la información del paciente', 'danger')
        return redirect(url_for('home'))
    
@main.route('/<num_doc>/editar', methods=['GET', 'POST'])
def editar_paciente(num_doc):
    if request.method == 'GET':
        try:
            paciente = PacienteModel.get_paciente(num_doc)
            if paciente is not None:
                return render_template('paciente_info.html', paciente=paciente)
            else:
                flash('Paciente no encontrado', 'danger')
                return redirect(url_for('paciente_blueprint.get_pacientes'))
        except Exception as ex:
            flash('Error al obtener la información del paciente', 'danger')
            return redirect(url_for('paciente_blueprint.get_pacientes'))
    elif request.method == 'POST':
        try:
            # Recuperar datos del formulario
            nombre = request.form.get('nombre')
            apellido = request.form.get('apellido')
            email = request.form.get('email')
            telefono = request.form.get('telefono')
            localidad = request.form.get('localidad')
            domicilio = request.form.get('domicilio')

            if PacienteModel.actualizar_paciente(num_doc, nombre, apellido, email, telefono, localidad, domicilio):
                flash('Información del paciente actualizada correctamente', 'success')
            else:
                flash('Error al actualizar la información del paciente', 'danger')

            flash('Información del paciente actualizada correctamente', 'success')
            return redirect(url_for('paciente_blueprint.get_pacientes'))
        except Exception as ex:
            flash('Error al actualizar la información del paciente', 'danger')
            return redirect(url_for('paciente_blueprint.get_pacientes'))
