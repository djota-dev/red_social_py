from datetime import datetime

class Publicacion:
    
    def __init__(self, usuario, contenido):
        self.usuario = usuario
        self.contenido = contenido
        self.fecha = datetime.now()
        
        
    def __str__(self):
        return f"{self.usuario.nombre} ({self.fecha}: {self.contenido})"
            