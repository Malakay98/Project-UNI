from datetime import datetime
from datos.modelos import usuario as modelo_usuario


def userExist(username, email, password):
    usuarios = modelo_usuario.login(username, email, password)
    return not len(usuarios) == 0


def createSession(id_usuario):
    current_time = datetime.now()
    dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario.createSession(id_usuario, dt_string)


def getUsers():
    return modelo_usuario.getUsers()


def GetUserById(id_usuario):
    usuarios = modelo_usuario.getOneUser(id_usuario)
    if len(usuarios) == 0:
        raise Exception("El usuario no existe")
    return usuarios[0]


def createUsers(username, email, firstName, lastName, password):
    return modelo_usuario.createUsers(username, email, firstName, lastName, password)


def editUsers(id_usuario, datos_usuario):
    return modelo_usuario.editUser(id_usuario, datos_usuario)


def deleteUser(id_usuario):
    return modelo_usuario.deleteUser(id_usuario)


def login(username, email, password):
    if userExist(username, email, password):
        usuario = modelo_usuario.login(username, email, password)[0]
        return createSession(usuario['idUsers'])
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