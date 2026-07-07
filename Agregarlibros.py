    def agregar_libro(self):
        id = int(input("ID: "))
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        seccion = input("Sección: ")

        nuevo = Libro(
            id,
            titulo,
            autor,
            categoria,
            seccion
        )

        self.libros.append(nuevo)

        print("Libro agregado correctamente.")