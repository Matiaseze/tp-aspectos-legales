from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for

#Modelos
from models.UsuarioModel import UsuarioModel

main=Blueprint('usuario_blueprint',__name__)

@main.route('/')
def get_usuarios():
    try:
        usuarios=UsuarioModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message' : str(ex)}),500
    
@main.route('/<id>')
def get_usuario(id):
    try:
        usuario=UsuarioModel.get_usuario(id)
        if usuario is not None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message' : str(ex)}),500