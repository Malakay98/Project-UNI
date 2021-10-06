import sqlite3


sql_tabla_noticias = '''
CREATE TABLE IF NOT EXISTS Noticias(
    idNews INTEGER PRIMARY KEY,
    idUser INTEGER,
    description TEXT,
    photo TEXT,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(idNews, idUser)
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers) ON DELETE CASCADE
)
'''


sql_tabla_comentarios = '''
CREATE TABLE IF NOT EXISTS Comentarios(
    id INTEGER PRIMARY KEY,
    idUser INTEGER,
    idPost INTEGER
    content TEXT,
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers),
    FOREIGN KEY(idPost) REFERENCES Noticias(idNews)
)
'''


sql_tabla_rol = '''
CREATE TABLE IF NOT EXISTS Rol(
    idRol INTEGER PRIMARY KEY, 
    rolDescription TEXT
)
'''


sql_tabla_admins = '''
CREATE TABLE IF NOT EXISTS Administradores(
    idAdmin INTEGER PRIMARY KEY,
    idUser INTEGER,
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers)    
)
'''


sql_tabla_users = '''
CREATE TABLE IF NOT EXISTS Usuarios(
    idUsers INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT,
    firstName TEXT,
    lastName TEXT,
    id_Rol INTEGER,
    photo TEXT,
    FOREIGN KEY(id_Rol) REFERENCES Rol(idRol) 
)
'''


sql_tabla_sesiones = '''
CREATE TABLE IF NOT EXISTS Sesiones(
    idSessions INTEGER PRIMARY KEY,
    idUser INTEGER,
    date_time TEXT,
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers)
)
'''


sql_eliminar_tabla = '''
DROP TABLE Publicaciones
'''


if __name__ == '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('Universidad.db')

        print('Creando Tablas..')
        conexion.execute(sql_eliminar_tabla)
        print("Tabla eliminada")
        conexion.execute(sql_tabla_noticias)
        print("Tabla noticias creada satisfactoriamente")
        conexion.execute(sql_tabla_comentarios)
        print('Tabla comentarios creada satisfactoriamente')
        conexion.execute(sql_tabla_rol)
        print("Tabla roles creada satisfactoriamente")
        conexion.execute(sql_tabla_admins)
        print("Tabla administradores creada satisfactoriamente")
        conexion.execute(sql_tabla_users)
        print("Tabla usuarios creada satisfactoriamente")
        conexion.execute(sql_tabla_sesiones)
        print("Tabla sesiones creada satisfactoriamente")
        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)