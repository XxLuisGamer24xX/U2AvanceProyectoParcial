from guardarEnMongo import * 
from demostrativoPyQt5 import *
class Usuarios():
    '''
    class Usuarios():
        Clase que Padre que contiene los atributos de los usuarios y métodos para registrar y iniciar sesión 
    Atributos:
        nombre: string
        apellido: string
        usuario: string
        email: string
        contraseña: string
    -------------------------
    Métodos:
        def __init__(self, usuario, contraseña,nombre ,apellido, email):
    '''
    usuarios=retornarUsuarios()
    contraseñas=retornarContraseñas()
    def __init__(self, usuario, contraseña,nombre ,apellido, email, cedula ):
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.cedula=cedula
