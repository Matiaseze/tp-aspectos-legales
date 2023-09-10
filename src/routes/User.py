from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required


#Modelos
from models.UsuarioModel import UsuarioModel

#Entidades
from models.entities.Usuario import Usuario

main=Blueprint('user_blueprint',__name__)
# login_manager_app = LoginManager(main)

# @login_manager_app.user_loader
# def load_user(id):
#     return UsuarioModel.get_usuario(id)

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Usuario(0, request.form['username'], request.form['password'])
        logged_user = UsuarioModel.login(user)

        if logged_user is not None:
            if logged_user.clave:
                print(logged_user.id)
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')