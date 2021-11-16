from flask import Flask, request, jsonify, json
from servicios.autenticacion import autenticacion
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def getIndex():
    return render_template('index.html')





# ||| USUARIOS |||






# Obtener los datos de todos los usuarios.
@app.route('/usuarios', methods=['GET'])  # Funciona
def obtener_usuarios():
    return jsonify(autenticacion.getUsers())


# Obtener los datos de un usuario mediante su ID "idUsers"
@app.route('/usuarios/<id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    try:
        usuario = autenticacion.GetUserById(id_usuario)
        return jsonify(usuario)
    except Exception:
        return 'Usuario no encontrado', 404


# Crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])  # Funciona
def crear_usuario():
    datos_usuario = request.get_json()
    if 'username' not in datos_usuario or datos_usuario['username'] == '':
        return 'El nombre de usuario es requerido', 400  # Informa que la sintaxis de la petición no es la correcta por lo que el servidor no es capaz de entender la petición del navegador. Se encuentra entre uno de los errores más comunes.
    if 'email' not in datos_usuario or datos_usuario['email'] == '':
        return 'El email es requerido', 400
    if 'firstName' not in datos_usuario or datos_usuario['firstName'] == '':
        return 'El nombre es requerido', 400
    if 'lastName' not in datos_usuario or datos_usuario['lastName'] == '':
        return 'El apellido es requerido', 400
    if 'password' not in datos_usuario or datos_usuario['password'] == '':
        return 'La clave es requerida', 400
    autenticacion.createUsers(datos_usuario['username'], datos_usuario['email'], datos_usuario['firstName'],
                              datos_usuario['lastName'], datos_usuario['password'])
    return jsonify(f'Usuario creado exitosamente. Usuario: ',
                   datos_usuario), 200  # Codigo de estado "200": informa que todo se ha procesado de manera correcta.


# Modificar los valores de un usuario
@app.route('/usuarios/<id_usuario>', methods=['PUT'])  # Funciona
def modificar_usuario(id_usuario):
    datos_usuario = request.get_json()
    if 'username' not in datos_usuario or datos_usuario['username'] == '':
        return "El nombre de usuario es requerido", 400
    if 'firstName' not in datos_usuario or datos_usuario['firstName'] == '':
        return "El nombre es requerido", 400
    if 'lastName' not in datos_usuario or datos_usuario['lastName'] == '':
        return "El apellido es requerido", 400
    if 'password' not in datos_usuario or datos_usuario['password'] == '':
        return "La clave es requerida", 400
    autenticacion.editUsers(id_usuario, datos_usuario)
    return 'Usuario modificado', 200


# Elimina al usuario a partir del ID del mismo
@app.route('/usuarios/<id_usuario>', methods=['DELETE'])  # Funciona
def eliminar_usuario(id_usuario):
    autenticacion.deleteUser(id_usuario)
    return jsonify(f'Usuario eliminado. ID del usuario: ', id_usuario), 200





# ||| FORO |||







@app.route('/foro', methods=['GET'])  # Funciona
def obtener_foros():
    return jsonify(autenticacion.getForums())


@app.route('/foro/<id_forum>', methods=['GET'])  # Funciona
def obtener_foro(id_forum):
    try:
        foro = autenticacion.getForum(id_forum)
        if not foro:
            return 'Foro no existente', 404
        return jsonify(foro)
    except Exception:
        return 'Error en el servidor', 500  # Indica que algo ha salido mal en el servidor



@app.route('/foro', methods=['GET', 'POST'])  # Funciona
def crear_foro():
    datos_foro = request.get_json()
    if 'title' not in datos_foro:
        return 'Falta un titulo', 400
    if 'content' not in datos_foro:
        return 'La descripcion no puede estar vacia', 400
    autenticacion.createForum(datos_foro['title'], datos_foro['content'])
    return jsonify('Publicacion creada exitosamente', datos_foro), 200



@app.route('/foro/<id_forum>', methods=['DELETE'])  # Funciona
def eliminar_foro(id_forum):
    autenticacion.deleteForum(id_forum)
    return jsonify('Publicacion eliminada. Publicacion: ', id_forum), 200


@app.route('/foro/<id_forum>', methods=['PUT'])  # Funciona
def editar_foro(id_forum):
    datos_foro = request.get_json()
    if 'title' not in datos_foro or datos_foro['title'] == '':
        return "Escribe un nuevo titulo", 400
    if 'content' not in datos_foro or datos_foro['content'] == '':
        return "Escribe una nueva descripcion", 400
    autenticacion.editForum(id_forum, datos_foro)
    return "Publicacion modificada", 200






# ||| NOTICIAS |||







@app.route('/noticias', methods=['GET'])
def obtener_las_noticias():
    return jsonify(autenticacion.getAllNews())


@app.route('/noticias/<id_new>', methods=['GET'])
def obtener_una_noticia(id_new):
    try:
        noticia = autenticacion.getOneNew(id_new)
        if not noticia:
            return "Noticia no existente", 404
        return jsonify(noticia)
    except Exception:
        return "Error en el servidor", 500


@app.route('/noticias', methods=['POST'])
def crear_noticia():
    datos_news = request.get_json()
    if 'title' not in datos_news:
        return 'Por favor escriba un titulo', 400  # indica que el servidor no puede o no quiere procesar la solicitud debido a algo que se percibe como un error del cliente
    if 'description' not in datos_news:
        return 'Por favor escriba una descripcion', 400
    if 'photo' not in datos_news:
        return 'Se necesita una foto', 400
    autenticacion.createNew(datos_news['title'], datos_news['description'], datos_news['photo'])
    return jsonify(f'Noticia creada', datos_news), 200


@app.route('/noticias/<id_new>', methods=['DELETE'])
def eliminarNoticia(id_new):
    autenticacion.deleteNew(id_new)
    return jsonify('Noticia eliminada exitosamente'), 200


@app.route('/noticias/<id_new>', methods=['PUT'])
def editar_noticia(id_new):
    datos_noticias = request.get_json()
    if 'title' not in datos_noticias or datos_noticias['title'] == '':
        return "Porfavor, modifica el titulo", 400
    if 'description' not in datos_noticias or datos_noticias['description'] == '':
        return "Porfavor, modifica la descripcion", 400
    autenticacion.editNew(id_new, datos_noticias)
    return "Noticia modificada", 200




# ||| LOGIN |||




# Iniciamos sesion con un usuario existente

@app.route('/login', methods=['POST'])  # Funciona
def login():
    datos_usuario = request.get_json()
    if 'username' not in datos_usuario:
        return 'El usuario es requerido', 400
    if 'password' not in datos_usuario:
        return 'La clave es requerida', 400
    id_sesion = autenticacion.login(datos_usuario['username'], datos_usuario['password'])
    if id_sesion:
        return f"Usuario logueado exitosamente: idSession {id_sesion}", 200
    else:
        return f"Usuario, correo o clave equivocada, intentelo de nuevo", 400


if __name__ == '__main__':
    app.debug = True
    app.run(port=2400)
