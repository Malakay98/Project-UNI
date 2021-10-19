from datos.base_de_datos import BaseDeDatos

def getAllNews():
    obtener_noticias = f'''
    SELECT * FROM Publicaciones
    '''
    bd = BaseDeDatos()
    return [{'idPost': registro[0],
             'idUser': registro[1],
             'description': registro[2],
             'photo': registro[3],
             'createdAt': registro[4]
             } for registro in bd.ejecutar_sql(obtener_noticias)]


def getOneNew(id_post):
    obtener_una_noticias = f'''
    SELECT * FROM Publicaciones
    WHERE idPost = {id_post}
    '''
    bd = BaseDeDatos()
    return[{'idPost': registro[0],
             'idUser': registro[1],
             'description': registro[2],
             'photo': registro[3],
             'createdAt': registro[4]
             } for registro in bd.ejecutar_sql(obtener_una_noticias)]


def saveNew(id_post, content):
    crear_noticia = f'''
    INSERT INTO Noticias (idNews, description)
    VALUES({id_post}, {content})
    '''
    bd = BaseDeDatos()
    return[{'idPost': registro[0],
             'idUser': registro[1],
             'description': registro[2]
             } for registro in bd.ejecutar_sql(crear_noticia)]

def deleteNew(id_post):
    eliminar_noticia = f'''
    DELETE FROM Noticias
    WHERE idNews = {id_post}
    '''
    db = BaseDeDatos()
    return db.ejecutar_sql(eliminar_noticia)


def editNew(id_post, content):
    editar_noticia = f'''
    UPDATE Noticias
    SET description = {content}
    WHERE idNews = {id_post}
    '''
    db = BaseDeDatos()
    return db.ejecutar_sql(editar_noticia)


def getComments(id_comment):
    obtener_comentarios = f'''
    SELECT * FROM Comentarios
    WHERE idPost = {id_comment}
    '''
    db = BaseDeDatos()
    return[{'id': registro[0],
            'idPost': registro[1],
            'idUser': registro[2],
            'content': registro[3]
            } for registro in db.ejecutar_sql(obtener_comentarios)]


def createComment(id_user, id_post, content):
    crear_comentario = f'''
    INSERT INTO Comentarios (idUser, idPost, content)
    VALUES ({id_user}, {id_post}, {content})
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_comentario)


def deleteComment(id):
    eliminar_comentario = f'''
    DELETE FROM Comentarios
    WHERE id = {id}
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_comentario)


def editComment(id, content):
    modificar_comentario = f'''
    UPDATE Comentarios
    SET content = {content}
    WHERE id = {id}
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_comentario)


