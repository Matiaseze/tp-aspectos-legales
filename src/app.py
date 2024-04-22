from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from utils.auth_confirm import confirm_token, generate_confirmation_token
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail, Message
from database.db import get_connection
#Rutas
from routes import Usuario, Paciente, Medico
#Modelos
from models.UsuarioModel import UsuarioModel

from models.entities.Usuario import Usuario as User

app = Flask(__name__)
csrf=CSRFProtect()

login_manager_app = LoginManager(app)

db = get_connection()

@login_manager_app.user_loader
def load_user(id):
    return UsuarioModel.get_usuario_id(id)

# Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'MAIL_USR'
app.config['MAIL_PASSWORD'] = 'MAIL_PSSWRD'
app.config['MAIL_DEFAULT_SENDER'] = '(John Doe, johndoe@jdoe.com)'
mail = Mail(app)


# RUTAS 
@app.route('/')
def inicio():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = UsuarioModel.login(user)

        if logged_user is not None:
            if logged_user.t_usuario == 1:
                if not logged_user.is_confirmed:
                    flash("El usuario no está confirmado. Por favor, verifica tu correo electrónico.", 'danger')
                    return render_template('auth/login.html')

            if logged_user.clave:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Usuario o contraseña incorrecta")
        else:
            flash("Usuario o contraseña incorrecta")
            return render_template('auth/login.html')
    # Si no es POST es GET
    return render_template('auth/login.html')

@app.route('/signup')
def signup():
    return render_template('auth/register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Recopilar datos del formulario
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        user = User(id=0, usuario=username,clave=password, mail=email, t_usuario=1, is_confirmed=False)

        if user is not None:
            print ('si usuario con el mismo mail y mismo nombre de usuario existe')
            UsuarioModel.add_usuario(user)


        token = generate_confirmation_token(user.mail)
        confirm_url = url_for('confirm_email', token=token, _external=True)
    
        msg = Message('Confirma tu cuenta', recipients=[user.mail])
        msg.body = f'Para confirmar tu cuenta, haz clic en el siguiente enlace: {confirm_url}'
    
        mail.send(msg)
    flash('Se ha enviado un correo de confirmación a tu dirección de correo electrónico.', 'success')
    return redirect(url_for('login'))



@app.route('/confirm/<token>')
# Funcion para confimar correo
def confirm_email(token):
    email = confirm_token(token)
    
    if not email:
        flash('El enlace de confirmación es inválido o ha expirado.', 'danger')
        return redirect(url_for('login'))
    
    usuario = UsuarioModel.get_usuario_mail(email)
    print('DEBUG: confirm_mail')
    print(usuario.is_confirmed)

    flash (UsuarioModel.user_confirmed(usuario))

    return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    logout_user()
    return render_template('auth/login.html')

@app.route('/home')
@login_required
def home():
    tipo_usuario = UsuarioModel.get_tipo_usuario(current_user.usuario)
    return render_template('home.html', tipo_usuario=tipo_usuario)

def page_not_found(error):
    return "<h1>Pagina no encontrada :/</h1>", 404

def pag_unauthorized(error):
    flash("Debe ingresar sus credenciales")
    return redirect(url_for('login'))

#Blueprints
app.register_blueprint(Usuario.main, url_prefix=('/usuarios'))
app.register_blueprint(Paciente.main, url_prefix=('/pacientes'))
app.register_blueprint(Medico.main, url_prefix=('/medicos'))

if __name__ == '__main__' :

    app.config.from_object(config['development'])
    
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['SECURITY_PASSWORD_SALT'] = '29$9VZ@!9RknEh4m'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@dbpg:5432/flask-restapi'
    csrf.init_app(app)
    #Manejador, error 404
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(401, pag_unauthorized)

    app.run(host="0.0.0.0", port=7000)
