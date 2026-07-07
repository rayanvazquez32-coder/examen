    def devolver_libro(self):

        id_usuario = int(input("ID Usuario: "))
        id_libro = int(input("ID Libro: "))

        for usuario in self.usuarios:

            if usuario.id == id_usuario:

                if id_libro in usuario.libros_prestados:

                    usuario.libros_prestados.remove(
                        id_libro
                    )

                    for libro in self.libros:
                        if libro.id == id_libro:
                            libro.disponible = True

                    print("Libro devuelto.")
                    return

        print("No se pudo devolver el libro.")