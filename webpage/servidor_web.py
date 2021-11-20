from flask import Flask, request, redirect, url_for, session
from flask import render_template
from time import time
import json
from webpage.servicios import autenticacion
import os.path
import os

app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

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
            error = 'Credenciales Invalidas'
        else:
            session['username'] = request.form['username']
            session['idUsers'] = credenciales
            return redirect(url_for('home'))
    return render_template('login.html', error = error)


@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    return render_template("profile.html")


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
            return redirect(url_for('login'))
    return render_template('register.html', error = error)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


# Problema principal, no puedo crear una publicacion que se muestre en la misma pagina del foro
@app.route('/forum', methods=['GET', 'POST'])
def forum():
    error = None
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        if not autenticacion.crear_foro(
            session['idUsers'],
            request.form['title'],
            request.form['content']):
            error = "No se pudo crear la publicacion"
        else:
            return redirect(url_for('forum'))
    return render_template('forum.html', error = error)


@app.route('/forum/<id_forum>', methods = ['GET', 'POST'])
def oneForum():
    if request.method == 'GET':
        return render_template('oneForum.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port = 3000)