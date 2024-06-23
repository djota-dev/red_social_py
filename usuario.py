class Usuario:
    
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.publicaciones = [] #acá se almacenará las publicaciones de los usuarios
        
        
    def crear_publicacion(self, contenido):
        from publicacion import Publicacion
        publicacion = Publicacion(self,contenido)
        self.publicaciones.append(publicacion)
        return publicacion
    
    
    def mostrar_publicaciones(self):
        if not self.publicaciones:
            print(f"{self.nombre} no tiene publicaciones")
        else:
            for publicacion in self.publicaciones:
                print(publicacion)
                
                