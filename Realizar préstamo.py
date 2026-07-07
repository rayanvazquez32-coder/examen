    def prestar_libro(self):

        id_usuario = int(input("ID Usuario: "))
        id_libro = int(input("ID Libro: "))

        usuario_encontrado = None
        libro_encontrado = None

        # Buscar usuario
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                usuario_encontrado = usuario

        # Buscar libro
        for libro in self.libros:
            if libro.id == id_libro:
                libro_encontrado = libro

        if usuario_encontrado is None:
            print("Usuario no existe.")
            return

        if libro_encontrado is None:
            print("Libro no existe.")
            return

        # Máximo de 3 libros
        if len(usuario_encontrado.libros_prestados) >= 3:
            print("El usuario ya tiene 3 libros.")
            return

        # Validar disponibilidad
        if libro_encontrado.disponible is False:
            print("El libro no está disponible.")
            return

        # Registrar préstamo
        usuario_encontrado.libros_prestados.append(
            libro_encontrado.id
        )

        usuario_encontrado.total_prestamos += 1

        libro_encontrado.disponible = False
        libro_encontrado.veces_prestado += 1

        fecha = datetime.now().strftime("%d/%m/%Y")

        registro = (
            f"Usuario: {usuario_encontrado.nombre} | "
            f"Libro: {libro_encontrado.titulo} | "
            f"Fecha: {fecha}"
        )

        self.historial.append(registro)

        print("Préstamo realizado.")