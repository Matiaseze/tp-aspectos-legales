from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for#, current_app
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_mail import Message
from flask import current_app as app
from itsdangerous import URLSafeTimedSerializer, BadSignature
from flask_wtf.csrf import CSRFProtect


#Modelos
from models.UsuarioModel import UsuarioModel

#Entidades
from models.entities.Usuario import Usuario

auth=Blueprint('user_blueprint', __name__)
csrf = CSRFProtect()

@auth.route('/', methods=['GET', 'POST'])
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
        return render_template('auth/home.html')
    
@auth.route('/signup2', methods=['GET', 'POST'])
@csrf.exempt
def register():
    if request.method == 'POST':
        # Recopilar datos del formulario
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        print('DEBUG')
        print(f'Usuario: {username}, Email: {email}, Contraseña: {password}')

        # Crear un usuario en la base de datos
        user = Usuario(id=0, nombre=username, mail=email, clave=password, is_confirmed=False, t_usuario=1)
        if user is not None:
            UsuarioModel.add_usuario(user)


        token = generate_confirmation_token(user.mail)
        confirm_url = url_for('user_blueprint.confirm_email', token=token, _external=True)
    
        msg = Message('Confirma tu cuenta', recipients=[user.mail])
        msg.body = f'Para confirmar tu cuenta, haz clic en el siguiente enlace: {confirm_url}'
    
        mail = app.get_mail()
        mail.send(msg)
    flash('Se ha enviado un correo de confirmación a tu dirección de correo electrónico.', 'success')
    return redirect(url_for('auth.login'))

# Metodo para generar token de confirmacion
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

# Funcion para confimar correo

@auth.route('/confirm/<token>')
def confirm_email(token):
    email = confirm_token(token)
    
    if not email:
        flash('El enlace de confirmación es inválido o ha expirado.', 'danger')
        return redirect(url_for('auth.login'))
    
    user = Usuario.query.filter_by(email=email).first_or_404()

    flash (Usuario.user_confirmed(user))

    return redirect(url_for('auth.login'))
    
# Funcion para confimar token

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=expiration)
    except BadSignature:
        return False
    return email

