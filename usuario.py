class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []
        self.total_prestamos = 0