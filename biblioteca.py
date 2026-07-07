import json
from libro import Libro
from usuario import Usuario
from datetime import datetime


class Biblioteca:

    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.historial = []

        # Mapa de la biblioteca
        self.grafo = {
            "Entrada": ["A"],
            "A": ["Entrada", "B", "C"],
            "B": ["A", "D"],
            "C": ["A"],
            "D": ["B"]
        }