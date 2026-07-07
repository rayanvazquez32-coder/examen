class Libro:
    def __init__(self, id, titulo, autor, categoria, seccion):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.seccion = seccion
        self.disponible = True
        self.veces_prestado = 0