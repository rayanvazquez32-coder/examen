    def cambiar_estado(self):

        id = int(input("ID del libro: "))

        for libro in self.libros:

            if libro.id == id:

                libro.disponible = not libro.disponible
                print("Estado actualizado.")
                return

        print("Libro no existe.")