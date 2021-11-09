from flask import Flask, request, redirect, url_for, session
from flask import render_template
from webpage.servicios import autenticacion

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        if not autenticacion.validar_credenciales(
                request.form['email'],
                request.form['password']):
            error = 'Credenciales Invalidas'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error = error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        if not autenticacion.crear_usuario(
            request.form['username'], 
            request.form['email'], 
            request.form['firstName'],
            request.form['lastName'], 
            request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('home'))
    return render_template('register.html', error = error)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')



@app.route('/forum', methods=['GET', 'POST'])
def forum():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_foro(
            request.form['title'], 
            request.form['content']):
            error = 'No se pudo crear la publicacion'
        else:
            return redirect(url_for('home'))
    return render_template('forum.html', error = error)


if __name__ == '__main__':
    app.debug = True
    app.run(port = 3000)