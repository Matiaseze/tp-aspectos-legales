from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
from flask_login import current_user
#Modelos
from models.MedicoModel import MedicoModel


main=Blueprint('medico_blueprint',__name__)


@main.route('/')
def get_medicos():
    try:
        medicos=MedicoModel.get_medicos()
        return jsonify(medicos)
    except Exception as ex:
        return jsonify({'message' : str(ex)}),500
    
@main.route('/<id>')
def get_medico(id):
    try:
        medico=MedicoModel.get_medico(id)
        if medico is not None:
            return jsonify(medico)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message' : str(ex)}),500
    
@main.route('/info')
def ver_info_medico():
    try:
        id = current_user.id
        
        medico = MedicoModel.get_medico(id)
        
        if medico is not None:
            return render_template('medicos/mi_info.html', medico=medico)
        else:
            flash('medico no encontrado', 'danger')

    except Exception as ex:
        flash('Error al obtener la información del medico', 'danger')
        return redirect(url_for('home'))
    
@main.route('/<id>/modificar', methods=['GET', 'POST'])

def modificar_medico(id):
    if request.method == 'GET':
        try:
  
            medico = MedicoModel.get_medico(id)

            if medico is not None:

                return render_template('medicos/modificar_medico.html', medico=medico)
            else:
                flash('medico no encontrado', 'danger')
                return redirect(url_for('home'))
        except Exception as ex:

            flash('Error al obtener la información del medico', 'danger')
            return redirect(url_for('home'))
    elif request.method == 'POST':
        try:
            # Recuperar datos del formulario
            documento = request.form.get('documento')
            nombre = request.form.get('nombre')
            apellido = request.form.get('apellido')
            legajo = request.form.get('legajo')
            email = request.form.get('email')
            telefono = request.form.get('telefono')
            domicilio = request.form.get('domicilio')

            if MedicoModel.actualizar_medico(id, documento, nombre, apellido,legajo, email, telefono, domicilio):
                flash('Información del medico actualizada correctamente', 'success')
            else:
                flash('Error al actualizar la información del medico', 'danger')

            return redirect(url_for('home'))
        except Exception as ex:

            flash('Error al actualizar la información del medico', 'danger')
            return redirect(url_for('home'))
