from datos.base_de_datos import BaseDeDatos

def getAllNews():
    obtener_noticias = f'''
    SELECT idNews, idUser, title, description, photo FROM Noticias
    '''
    bd = BaseDeDatos()
    return bd.ejecutar_sql(obtener_noticias)


def getOneNew(id_new):
    obtener_una_noticia = f'''
    SELECT idNews, idUser, title, description, photo
    FROM Noticias
    WHERE idNews = {id_new}
    '''
    bd = BaseDeDatos()
    result = bd.ejecutar_sql(obtener_una_noticia)
    if result:
        return {'idPost': result[0][0],
                 'idUser': result[0][1],
                 'title': result[0][2],
                 'description': result[0][3],
                 'photo': result[0][4]}
    else:
        return None


def createNew(title, content, photo):
    crear_noticia_sql = f'''
       INSERT INTO Noticias (title, description, photo)
       VALUES('{title}', '{content}', '{photo}')
    '''
    bd = BaseDeDatos()
    return [{
             'title': registro[0],
             'description': registro[1],
             'photo': registro[2]}
             for registro in bd.ejecutar_sql(crear_noticia_sql)]


def deleteNew(id_post):
    eliminar_noticia = f'''
    DELETE FROM Noticias
    WHERE idNews = {id_post}
    '''
    db = BaseDeDatos()
    return db.ejecutar_sql(eliminar_noticia)


def editNew(id_post, datos_noticias):
    editar_noticia = f'''
    UPDATE Noticias
    SET title = '{datos_noticias["title"]}', description = '{datos_noticias["description"]}'
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


