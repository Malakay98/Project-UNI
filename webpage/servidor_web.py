from flask import Flask, request, redirect, url_for, session, render_template
import requests
from werkzeug.utils import secure_filename
from time import time
import os
import urllib.request
from webpage.servicios import autenticacion



UPLOAD_FOLDER = '/static/img/upload/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'BAD_SECRET_KEY'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Aqui estuvimos teniendo muchos cambios con el session. Luego de estos cambios, dejo de funcionar mi Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        credenciales = autenticacion.validar_credenciales(
            request.form['username'],
            request.form['password'])
        if credenciales == None:
            print(credenciales)
            error = 'Credenciales Invalidas'
        else:
            session['username'] = request.form['username']
            session['idUsers'] = credenciales
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('index'))


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not session:
        return redirect(url_for('login'))
    if request.method == 'GET':
        usuario = autenticacion.obtener_usuario(session['idUsers'])
        return render_template("profile.html", usuario=usuario)
    else:
        return redirect(url_for('profile'))


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
                request.form['password'],
                request.form['phoneNumber']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/forum', methods=['GET', 'POST'])
def forum():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_foro(
                session['idUsers'],
                request.form['title'],
                request.form['content']):
            error = "No se pudo crear la publicacion"
        else:
            return redirect(url_for('forum'))
    else:
        posts = autenticacion.obtener_foros()
    return render_template('forum.html', error=error, posts=posts)


@app.route('/forum/delete/<id_forum>', methods=['GET'])
def deleteForum(id_forum):
    error = None
    if not autenticacion.eliminar_foro(id_forum):
        error = "No se pudo eliminar la publicacion"
    else:
        return redirect(url_for('forum'))
    return render_template('forum.html', error=error)


@app.route('/forum', methods=['DELETE'])
def delete(id_forum):
    if autenticacion.eliminar_foro(id_forum):
        return redirect(url_for('forum'))

# SUBIR FOTOS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    error = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('upload image filename: ' + filename)
            return render_template('profile.html', filename = filename)
        else:
            return redirect("Los archivos permitidos son: png, jpg y jpeg" + request.url, error = error)


@app.route('/display/<filename>', methods=['GET', 'POST'])
def display_image(filename):
    return redirect(url_for('static', filename='upload/' + filename), 301)

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
