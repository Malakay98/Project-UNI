import sqlite3


sql_tabla_noticias = '''
CREATE TABLE IF NOT EXISTS Noticias(
    idNews INTEGER PRIMARY KEY AUTOINCREMENT,
    idUser INTEGER,
    title TEXT,
    description TEXT,
    photo TEXT,
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers)
)
'''


sql_tabla_comentarios = '''
CREATE TABLE IF NOT EXISTS Comentarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idUser INTEGER,
    idPost INTEGER,
    content TEXT,
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers),
    FOREIGN KEY(idPost) REFERENCES Noticias(idNews)
)
'''


sql_tabla_rol = '''
CREATE TABLE IF NOT EXISTS Rol(
    idRol INTEGER PRIMARY KEY AUTOINCREMENT, 
    rolDescription TEXT
)
'''


sql_tabla_admins = '''
CREATE TABLE IF NOT EXISTS Administradores(
    idAdmin INTEGER PRIMARY KEY AUTOINCREMENT,
    idUser INTEGER,
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers)    
)
'''


sql_tabla_users = '''
CREATE TABLE IF NOT EXISTS Usuarios(
    idUsers INTEGER PRIMARY KEY AUTOINCREMENT,
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
    idSessions INTEGER PRIMARY KEY AUTOINCREMENT,
    idUser INTEGER,
    date_time TEXT,
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers)
)
'''

# 18/10/21 Creando nuevas tablas

sql_tabla_foro = '''
CREATE TABLE IF NOT EXISTS Foro(
    idForum INTEGER PRIMARY KEY AUTOINCREMENT,
    idUser INTEGER,
    title TEXT,
    content TEXT,
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers)
)
'''

sql_talba_comentarios_foro = '''
CREATE TABLE IF NOT EXISTS ComentariosForo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idForum INTEGER,
    idUser INTEGER,
    date_time TEXT,
    content TEXT,
    FOREIGN KEY(idForum) REFERENCES Foro(idForum),
    FOREIGN KEY(idUser) REFERENCES Usuarios(idUsers)
)
'''

sql_tabla_materias = '''
CREATE TABLE IF NOT EXISTS Materias(
    idCourse INTEGER PRIMARY KEY AUTOINCREMENT,
    courseName TEXT,
    professor TEXT,
    content TEXT
)
'''


sql_agregar_cosas = '''
ALTER TABLE Usuarios
ADD COLUMN region TEXT;
'''


if __name__ == '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('Universidad.db')
        cursor = conexion.cursor()

        print('Creando Tablas..')
        cursor.execute(sql_tabla_noticias)
        print("Tabla noticias creada satisfactoriamente")
        cursor.execute(sql_tabla_comentarios)
        print('Tabla comentarios creada satisfactoriamente')
        cursor.execute(sql_tabla_rol)
        print("Tabla roles creada satisfactoriamente")
        cursor.execute(sql_tabla_admins)
        print("Tabla administradores creada satisfactoriamente")
        cursor.execute(sql_tabla_users)
        print("Tabla usuarios creada satisfactoriamente")
        cursor.execute(sql_tabla_sesiones)
        print("Tabla sesiones creada satisfactoriamente")
        cursor.execute(sql_tabla_foro)
        print("Tabla foro creada exitosamente")
        cursor.execute(sql_talba_comentarios_foro)
        print("Tabla de comentarios del foro creada exitosamente")
        cursor.execute(sql_tabla_materias)
        print("Tabla materias creada exitosamente")
        cursor.execute(sql_agregar_cosas)
        print("Se ha actualizado la tabla Usuarios")
        cursor.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)