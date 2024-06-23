import json
from usuario import Usuario
from publicacion import Publicacion
from datetime import datetime

class RedSocial:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usuarios.append(usuario)
        return usuario

    def encontrar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email: 
                return usuario
        return None

    def mostrar_todas_publicaciones(self):
        for usuario in self.usuarios:
            usuario.mostrar_publicaciones()

    def guardar_datos(self, archivo):
        datos = []
        for usuario in self.usuarios:
            datos_usuario = {
                "nombre": usuario.nombre,
                "email": usuario.email,
                "publicaciones": [
                    {"contenido": pub.contenido, "fecha": pub.fecha.isoformat()}
                    for pub in usuario.publicaciones
                ]
            }
            datos.append(datos_usuario)
        with open(archivo, 'w') as f:
            json.dump(datos, f)

    def cargar_datos(self, archivo):
        with open(archivo, 'r') as f:
            datos = json.load(f)
        for datos_usuario in datos:
            usuario = self.registrar_usuario(datos_usuario["nombre"], datos_usuario["email"])
            for datos_pub in datos_usuario["publicaciones"]:
                publicacion = Publicacion(usuario, datos_pub["contenido"])
                publicacion.fecha = datetime.fromisoformat(datos_pub["fecha"])
                usuario.publicaciones.append(publicacion)
