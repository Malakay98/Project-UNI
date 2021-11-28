from datos.base_de_datos import BaseDeDatos

#Creo la funcion para obtener todos los usuarios.
#No necesito parametros en esta ocasion, por que no habran valores especificos que se necesiten para la peticion HTTP
def getUsers():
    obtener_usuarios_sql = f"""
       SELECT idUsers, username, email, firstName, lastName, password, id_Rol, region, city
       FROM Usuarios
    """
    # Llamo a la clase basededatos y la igualo con una variable
    bd = BaseDeDatos()
    #Devuelvo los valores que se obtuvieron de la peticion HTTP
    return [{'idUsers': registro[0],
             'username': registro[1],
             'email': registro[2],
             'firstName': registro[3],
             'lastName': registro[4],
             'password': registro[5],
             'id_Rol': registro[6],
             'region': registro[7],
             'city': registro[8]}
              #Por cada registro en la base de datos, quiero aplicar la variable con el metodo asignado
             for registro in bd.ejecutar_sql(obtener_usuarios_sql)]


def getOneUser(id_usuario):
    obtener_un_usuario_sql = f'''
       SELECT idUsers, username, email, firstName, lastName, photo, region, city
       FROM Usuarios
       WHERE idUsers = {id_usuario}
    '''
    bd = BaseDeDatos()
    return [{'idUsers': registro[0],
             'username': registro[1],
             'email': registro[2],
             'firstName': registro[3],
             'lastName': registro[4],
             'photo': registro[5],
             'region': registro[6],
             'city': registro[7]}
              #Por cada registro en la base de datos, quiero aplicar la variable con el metodo asignado
             for registro in bd.ejecutar_sql(obtener_un_usuario_sql)]

 
def createUsers(username, email, firstName, lastName, password, region, city):
    crear_usuario_sql = f"""
        INSERT INTO Usuarios(username, email, firstName, lastName, password, region, city)
        VALUES ('{username}', '{email}', '{firstName}', '{lastName}', '{password}', '{region}', '{city}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)



def createBiography(biography):
    crear_bio_sql = f"""
        INSERT INTO Usuarios(biography)
        VALUES('{biography}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_bio_sql)


def editUser(id_usuario, datos_usuario):
    modificar_usuario_sql = f'''
       UPDATE Usuarios
       SET username='{datos_usuario["username"]}', firstName='{datos_usuario["firstName"]}', lastName='{datos_usuario["lastName"]}', password='{datos_usuario["password"]}', photo='{datos_usuario["photo"]}'
       WHERE idUsers='{id_usuario}'
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)


def deleteUser(id_usuario):
    eliminar_usuario_sql = f'''
        DELETE
        FROM Usuarios
        WHERE idUsers = '{id_usuario}'
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_usuario_sql)

# Tambien podria usar "?" en vez de los parametros, esto para incluir mayor seguridad

def getUsersByFiveParamRegister(username, password):
    ingresar_datos_sql = f'''
       SELECT idUsers, username, email, firstName, lastName, password
       FROM Usuarios
       WHERE
       username = '{username}' AND password = '{password}'
    '''
    bd = BaseDeDatos()
    result = bd.ejecutar_sql(ingresar_datos_sql)
    if result:
        return {"idUsers": result[0][0],
                "username": result[0][1],
                "email": result[0][2],
                "firstName": result[0][3],
                "lastName": result[0][4],
                "password": result[0][5]}
    else:
        return None


def getUsersByTwoParamLogin(username, password):
    ingresar_datos = f'''
       SELECT idUsers, username, password
       FROM Usuarios
       WHERE
       username = '{username}' AND password = '{password}'
    '''
    bd = BaseDeDatos()
    result = bd.ejecutar_sql(ingresar_datos)
    if result:
        return {"idUsers": result[0][0],
                "username": result[0][1],
                "password": result[0][2]}
    else:
        return None

def createSession(idUser, dt_str):
    crear_sesion_sql = f'''
       INSERT INTO Sesiones(idUser, date_time)
       VALUES('{idUser}','{dt_str}')
    '''
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)


def getSession(id_sesion):
    obtener_sesion_sql = f'''
       SELECT idSessions, idUser, date_time 
       FROM Sesiones 
       WHERE idSessions = {id_sesion}
    '''
    bd = BaseDeDatos()
    return [{"idSessions": registro[0],
             "idUser": registro[1],
             "date_time": registro[2]
             } for registro in bd.ejecutar_sql(obtener_sesion_sql)]