import sqlite3
from sqlite3.dbapi2 import Cursor
from flask import Flask, request, jsonify
from servicios.autenticacion import autenticacion

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(autenticacion.getUsers())

# Crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'username' not in datos_usuario:
        return 'El nombre de usuario es requerido', 412 #Error "412"; El servidor no es capaz de cumplir con algunas de las condiciones impuestas por el "navegador" en nuestra petición​
    if 'email' not in datos_usuario:
        return 'El email es requerido', 412
    if 'password' not in datos_usuario:
        return 'La clave es requerida', 412
    autenticacion.crear_usuario(datos_usuario['username'], datos_usuario['email'], datos_usuario['password'])
    return jsonify(f'Usuario creado exitosamente. Usuario: ', datos_usuario), 200 #Codigo de estado "200": informa que todo se ha procesado de manera correcta.

@app.route('/usuarios', methods=['PUT'])
def modificar_usuario():
    pass

# Elimina al usuario a partir del email del mismo
@app.route('/usuarios/<id_usuario>', methods=['DELETE'])
def eliminar_usuario():
    email_usuario = request.get_json()
    if 'email' not in email_usuario:
        return 'El email es requerido para eliminar al usuario', 412
    autenticacion.eliminar_usuario(email_usuario['email'])
    return jsonify(f'Usuario eliminado. Email del usuario: ', email_usuario), 200

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
