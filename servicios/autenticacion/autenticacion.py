from datetime import datetime
from datos.modelos import usuario as modelo_usuario
from datos.modelos import noticias as modelo_noticias
from datos.modelos import foro as modelo_foro
from flask import session

# ||| USUARIOS |||


def getUsers():
    return modelo_usuario.getUsers()


def GetUserById(id_usuario):
    usuarios = modelo_usuario.getOneUser(id_usuario)
    if len(usuarios) == 0:
        raise Exception("El usuario no existe")
    return usuarios[0]


def createUsers(username, email, firstName, lastName, password, region, city):
    if not userExistforRegister(username, password):
        modelo_usuario.createUsers(username, email, firstName, lastName, password, region, city)
    else:
        raise Exception("Usuario ya existente")


def editUsers(id_usuario, datos_usuario):
    return modelo_usuario.editUser(id_usuario, datos_usuario)


def deleteUser(id_usuario):
    return modelo_usuario.deleteUser(id_usuario)

# || LOGIN Y VALIDACION DE USUARIO ||




def userExistforRegister(username, password):
    usuarios = modelo_usuario.getUsersByFiveParamRegister(username, password)
    return usuarios and len(usuarios) > 0


def createSession(id_usuario):
    current_time = datetime.now()
    dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario.createSession(id_usuario, dt_string)


def login(username, password):
    usuarios = modelo_usuario.getUsersByTwoParamLogin(username, password)
    if usuarios:
        session['idUser'] = usuarios['idUsers']
    else:
        raise Exception("El usuario no existe o la clave es invalida")


def validateSession(id_sesion):
    sesiones = modelo_usuario.getSession(id_sesion)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['date_time'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Sesion expirada
        return False
    else:
        return True


# ||| FORO |||

def getForums():
    return modelo_foro.getForums()


def getForum(id_forum):
    forum = modelo_foro.getOneForum(id_forum)
    return forum


def createForum(title, content, autor):
    print(title, content, autor)
    try:
        modelo_foro.createForum(title, content, autor)
    except:
        raise Exception("No se pudo crear la publicacion")


def deleteForum(id_forum):
    return modelo_foro.deleteForum(id_forum)


def editForum(id_forum, datos_foro):
    return modelo_foro.editForum(id_forum, datos_foro)


# ||| NOTICIAS |||

def getAllNews():
    return modelo_noticias.getAllNews()


def getOneNew(id_new):
    new = modelo_noticias.getOneNew(id_new)
    return new


def createNew(title, content, photo):
    return modelo_noticias.createNew(title, content, photo)


def deleteNew(id_new):
    return modelo_noticias.deleteNew(id_new)


def editNew(id_new, datos_noticias):
    return modelo_noticias.editNew(id_new, datos_noticias)