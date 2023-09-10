from flask import Flask, render_template, request, redirect, url_for
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required

#Rutas
from routes import Usuario, User
#Modelos
from models.UsuarioModel import UsuarioModel
app = Flask(__name__)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return UsuarioModel.get_usuario(id)



@app.route('/')
def login():
    return render_template('auth/login.html')

@app.route('/home')
def home():
    return render_template('home.html')

def page_not_found(error):
    return "<h1>Pagina no encontrada :/</h1>", 404

#Blueprints
app.register_blueprint(User.main, url_prefix=('/login'))
app.register_blueprint(Usuario.main, url_prefix=('/usuarios'))


if __name__ == '__main__' :
    app.config.from_object(config['development'])

    #Manejador, error 404
    app.register_error_handler(404, page_not_found)

    app.run(host="0.0.0.0", port=7000)
