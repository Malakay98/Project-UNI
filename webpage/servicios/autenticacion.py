from webpage.servicios import rest_api
import requests
from flask import session

def ingresar_inicio():
    respuesta = requests.post(f'{rest_api.API_URL}/index')
    return respuesta.json()



#Aca tambien tuvimos muchos cambios
def validar_credenciales(username, clave):
    body = {"username": username,
            "password": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    if respuesta.status_code == 200:
        return respuesta.text
    else:
        return None
    # Solo se verifica el codigo de la respuesta en este caso



def crear_usuario(usuario, email, nombre, apellido, clave, region, city):
    body = {"username": usuario,
            "email": email,
            "firstName": nombre,
            "lastName": apellido,
            "password": clave,
            "region": region,
            "city": city}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()


def obtener_usuario(id_usuario):
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios/{id_usuario}')
    return respuesta.json()


def crear_foro(autor, titulo, contenido):
    body = {
        "author": autor,
        "title": titulo,
        "content": contenido
    }
    respuesta = requests.post(f'{rest_api.API_URL}/forum', json = body)
    return respuesta.status_code == 200


def obtener_foros():
    respuesta = requests.get(f'{rest_api.API_URL}/forum')
    return respuesta.json()


def obtener_foro(id_forum):
    body = {
        crear_foro(id_forum)
    }
    respuesta = requests.post(f'{rest_api.API_URL}/forum', json = body)
    return respuesta.status_code == 200


def eliminar_foro(id_forum):
    body = {
        "idForum": id_forum
    }
    respuesta = requests.delete(f'{rest_api.API_URL}/forum/{id_forum}', json = body)
    return respuesta.status_code == 200
