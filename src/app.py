from flask import Flask, render_template, request, redirect, url_for
from config import config

#Rutas
from routes import Usuario

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')


def page_not_found(error):
    return "<h1>Pagina no encontrada :/</h1>", 404

#Blueprints
app.register_blueprint(Usuario.main, url_prefix=('/login'))


if __name__ == '__main__' :
    app.config.from_object(config['development'])

    #Manejador, error 404
    app.register_error_handler(404, page_not_found)

    app.run(host="0.0.0.0", port=7000)
