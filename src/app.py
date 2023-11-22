from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from utils.auth_confirm import confirm_token, generate_confirmation_token
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail, Message

#Rutas
from routes import Usuario, Paciente
#Modelos
from models.UsuarioModel import UsuarioModel

from models.entities.Usuario import Usuario as User

app = Flask(__name__)
csrf=CSRFProtect(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return UsuarioModel.get_usuario_id(id)

# Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'matyaseze777@gmail.com'
app.config['MAIL_PASSWORD'] = 'tdhn ksed kzpl pdkc'
app.config['MAIL_DEFAULT_SENDER'] = 'matyaseze777@gmail.com'
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

@app.route('/singup')
def singup():
    return render_template('auth/singup.html')

@app.route('/register', methods=['GET', 'POST'])
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
        user = User(id=0, nombre=username, mail=email, clave=password, is_confirmed=False, t_usuario=1)
        print('DEBUG')
        print (user)
        if user is not None:
            print('Usuario no es none')
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
    
    user = UsuarioModel.get_usuario_mail(email)
    print(user)
    flash (UsuarioModel.user_confirmed(user))

    return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    logout_user()
    return render_template('auth/login.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

def page_not_found(error):
    return "<h1>Pagina no encontrada :/</h1>", 404

def pag_unauthorized(error):
    flash("Debe ingresar sus credenciales")
    return redirect(url_for('login'))

#Blueprints
app.register_blueprint(Usuario.main, url_prefix=('/usuarios'))
app.register_blueprint(Paciente.main, url_prefix=('/pacientes'))


if __name__ == '__main__' :

    app.config.from_object(config['development'])
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['SECURITY_PASSWORD_SALT'] = '29$9VZ@!9RknEh4m'
    csrf.init_app(app)
    #Manejador, error 404
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(401, pag_unauthorized)

    app.run(host="0.0.0.0", port=7000)
