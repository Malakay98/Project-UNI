from datos.modelos import usuario as modelo_usuario

def getUsers():
    return modelo_usuario.getUsers()

def createUsers(username, email, password):
    return modelo_usuario.createUsers(username, email, password)

def deleteUser(id_usuario):
    return modelo_usuario.deleteUser(id_usuario)
