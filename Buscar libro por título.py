    def buscar_libro(self):

        nombre = input("Escribe el título: ")

        for libro in self.libros:

            if libro.titulo.lower() == nombre.lower():
                print("Libro encontrado")
                print("Autor:", libro.autor)
                print("Categoría:", libro.categoria)
                return libro

        print("Libro no encontrado.")
        return None