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