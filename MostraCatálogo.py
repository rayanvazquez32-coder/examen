    def mostrar_libros(self):

        if len(self.libros) == 0:
            print("No hay libros registrados.")
            return

        print("\nCATÁLOGO")

        for libro in self.libros:
            print("------------------")
            print("ID:", libro.id)
            print("Título:", libro.titulo)
            print("Autor:", libro.autor)
            print("Categoría:", libro.categoria)
            print("Disponible:", libro.disponible)