from datos.base_de_datos import BaseDeDatos


def getForums():
    obtener_foros_sql = f'''
       SELECT idForum, idUser, title, content 
       FROM Foro
    '''
    bd = BaseDeDatos()
    return [{
        'idForum': registro[0],
        'idUser': registro[1],
        'title': registro[2],
        'content': registro[3]
    } for registro in bd.ejecutar_sql(obtener_foros_sql)]


def getOneForum(id_forum):
    obtener_foro_sql = f'''
       SELECT title, content
       FROM Foro
       WHERE idForum = {id_forum}
    '''
    bd = BaseDeDatos()
    result = bd.ejecutar_sql(obtener_foro_sql)
    if result: 
        return {'title': result[0][0],
                'content': result[0][1]}
    else:
        return None



def createForum(title, content, autor):
    crear_foro_sql = f'''
       INSERT INTO Foro (title, content, idUser)
       VALUES('{title}', '{content}', '{autor}')
    '''
    print(crear_foro_sql)
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_foro_sql)



def deleteForum(id_forum):
    eliminar_foro_sql = f'''
       DELETE FROM Foro
       WHERE idForum = {id_forum}
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_foro_sql)


def editForum(id_forum, datos_foro):
    editar_publicacion_foro_sql = f'''
       UPDATE Foro
       SET content = '{datos_foro["content"]}', title = '{datos_foro["title"]}'
       WHERE idForum = {id_forum}
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(editar_publicacion_foro_sql)



def getCommentsForum(id_forum):
    obtener_comentarios_foro_sql = f'''
    SELECT * FROM ComentariosForo
    WHERE idForum = {id_forum}
    '''
    bd = BaseDeDatos()
    return[{'id': registro[0],
            'idForum': registro[1],
            'idUser': registro[2],
            'content': registro[3]
            } for registro in bd.ejecutar_sql(obtener_comentarios_foro_sql)]


def createCommentForum(id_user, id_forum, content):
    crear_comentario_foro = f'''
    INSERT INTO ComentariosForo (idUser, idForum, content)
    VALUES ({id_user}, {id_forum}, {content})
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_comentario_foro)


def deleteCommentForum(id):
    eliminar_comentario_foro = f'''
    DELETE FROM ComentariosForo
    WHERE id = {id}
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_comentario_foro)


def editCommentForum(id, content):
    modificar_comentario_foro = f'''
    UPDATE ComentariosForo
    SET content = {content}
    WHERE id = {id}
    '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_comentario_foro)