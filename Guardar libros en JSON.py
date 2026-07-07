    def guardar_libros(self):

        datos = []

        for libro in self.libros:

            datos.append({
                "id": libro.id,
                "titulo": libro.titulo,
                "autor": libro.autor,
                "categoria": libro.categoria,
                "seccion": libro.seccion,
                "disponible": libro.disponible,
                "veces_prestado": libro.veces_prestado
            })

        with open(
            "libros.json",
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )