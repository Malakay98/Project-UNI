from webpage.servicios import rest_api
import requests

def ingresar_inicio():
    respuesta = requests.post(f'{rest_api.API_URL}/index')
    return respuesta.json()


def validar_credenciales(email, clave):
    body = {"email": email,
            "password": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    # Solo se verifica el codigo de la respuesta en este caso
    return respuesta.status_code == 200


def crear_usuario(usuario, email, nombre, apellido, clave):
    body = {"username": usuario,
            "email": email,
            "firstName": nombre,
            "lastName": apellido,
            "password": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()


def crear_foro(titulo, contenido):
    body = {
        "title": titulo,
        "content": contenido
    }
    respuesta = requests.post(f'{rest_api.API_URL}/forum', json = body)
    return respuesta.status_code == 200

