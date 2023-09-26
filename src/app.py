from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
#Rutas
from routes import Usuario, User, Paciente
#Modelos
from models.UsuarioModel import UsuarioModel

app = Flask(__name__)
csrf=CSRFProtect()

login_manager_app = LoginManager(app)



@login_manager_app.user_loader
def load_user(id):
    return UsuarioModel.get_usuario(id)

# RUTAS 
@app.route('/')
def login():
    return render_template('auth/login.html')

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
app.register_blueprint(User.main, url_prefix=('/login'))
app.register_blueprint(Usuario.main, url_prefix=('/usuarios'))
app.register_blueprint(Paciente.main, url_prefix=('/pacientes'))

if __name__ == '__main__' :
    app.config.from_object(config['development'])
    csrf.init_app(app)
    #Manejador, error 404
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(401, pag_unauthorized)

    app.run(host="0.0.0.0", port=7000)
