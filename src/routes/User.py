from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
#Modelos
from models.UsuarioModel import UsuarioModel

#Entidades
from models.entities.Usuario import Usuario

main=Blueprint('user_blueprint',__name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Usuario(0, request.form['username'], request.form['password'])
        logged_user = UsuarioModel.login(user)

        if logged_user is not None:
            if logged_user.clave:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')
    
# @main.route('/registro', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Recopilar datos del formulario
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']

#         # Crear un usuario en la base de datos
#         user = User(username=username, email=email, password=password)

#         # Generar un token de confirmación y enviar el correo de confirmación
#         token = serializer.dumps(email, salt='email-confirm')
#         confirm_url = url_for('confirm_email', token=token, _external=True)
#         send_confirmation_email(email, confirm_url)


#         flash('Registro exitoso. Verifica tu correo para confirmar la cuenta.', 'success')
#         return redirect(url_for('login'))

#     return render_template('register.html')