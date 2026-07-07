    def libro_mas_prestado(self):

        if len(self.libros) == 0:
            return

        mayor = self.libros[0]

        for libro in self.libros:

            if libro.veces_prestado > mayor.veces_prestado:
                mayor = libro

        print("Libro más prestado:")
        print(mayor.titulo)