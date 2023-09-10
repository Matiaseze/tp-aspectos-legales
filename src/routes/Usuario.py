from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for

#Modelos
from models.UsuarioModel import UsuarioModel

#Entidades
from models.entities import Usuario

main=Blueprint('usuario_blueprint',__name__)


@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Usuario(0, request.form['username'],request.form['password'], 0,None )
        logged_user = UsuarioModel.login(user)
        if logged_user is not None:
            if logged_user.password:
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')

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
        print(usuario)
        if usuario is not None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404


    except Exception as ex:
        return jsonify({'message' : str(ex)}),500