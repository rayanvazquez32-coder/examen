    def encontrar_libro(self):

        nombre = input("Título del libro: ")

        for libro in self.libros:

            if libro.titulo.lower() == nombre.lower():

                ruta = self.buscar_ruta(
                    "Entrada",
                    libro.seccion
                )

                print("Ruta encontrada:")
                print(" -> ".join(ruta))
                return

        print("Libro no existe.")