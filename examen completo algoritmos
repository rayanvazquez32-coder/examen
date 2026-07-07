import json
from datetime import datetime

class Libro:
    def __init__(self, id, titulo, autor, categoria, seccion):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.seccion = seccion
        self.disponible = True
        self.veces_prestado = 0


class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []
        self.total_prestamos = 0


class Biblioteca:

    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.historial = []

        # Mapa de la biblioteca (Grafo)
        self.grafo = {
            "Entrada": ["A"],
            "A": ["Entrada", "B", "C"],
            "B": ["A", "D"],
            "C": ["A"],
            "D": ["B"]
        }

        self.cargar_datos()


    def agregar_libro(self):
        id = int(input("ID del libro: "))
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        seccion = input("Sección (A, B, C o D): ")

        libro = Libro(
            id,
            titulo,
            autor,
            categoria,
            seccion
        )

        self.libros.append(libro)
        print("Libro agregado correctamente.")

    def mostrar_libros(self):

        if len(self.libros) == 0:
            print("No hay libros registrados.")
            return

        print("\nCATÁLOGO DE LIBROS")

        for libro in self.libros:
            print("----------------------")
            print("ID:", libro.id)
            print("Título:", libro.titulo)
            print("Autor:", libro.autor)
            print("Categoría:", libro.categoria)
            print("Sección:", libro.seccion)
            print("Disponible:", libro.disponible)

    def buscar_libro(self):

        titulo = input("Título del libro: ")

        for libro in self.libros:

            if libro.titulo.lower() == titulo.lower():

                print("\nLibro encontrado")
                print("Autor:", libro.autor)
                print("Categoría:", libro.categoria)
                print("Sección:", libro.seccion)
                print("Disponible:", libro.disponible)
                return

        print("El libro no fue encontrado.")

    def cambiar_disponibilidad(self):

        id = int(input("ID del libro: "))

        for libro in self.libros:

            if libro.id == id:

                libro.disponible = not libro.disponible
                print("Disponibilidad actualizada.")
                return

        print("Libro no encontrado.")


    def agregar_usuario(self):

        id = int(input("ID del usuario: "))
        nombre = input("Nombre: ")

        usuario = Usuario(id, nombre)
        self.usuarios.append(usuario)

        print("Usuario registrado.")

    def prestar_libro(self):

        id_usuario = int(input("ID del usuario: "))
        id_libro = int(input("ID del libro: "))

        usuario = None
        libro = None

        for u in self.usuarios:
            if u.id == id_usuario:
                usuario = u

        for l in self.libros:
            if l.id == id_libro:
                libro = l

        if usuario is None:
            print("Usuario no existe.")
            return

        if libro is None:
            print("Libro no existe.")
            return

        if len(usuario.libros_prestados) >= 3:
            print("El usuario ya tiene 3 libros prestados.")
            return

        if libro.disponible is False:
            print("El libro no está disponible.")
            return

        usuario.libros_prestados.append(libro.id)
        usuario.total_prestamos += 1

        libro.disponible = False
        libro.veces_prestado += 1

        fecha = datetime.now().strftime("%d/%m/%Y")

        registro = (
            f"Usuario: {usuario.nombre} | "
            f"Libro: {libro.titulo} | "
            f"Fecha: {fecha}"
        )

        self.historial.append(registro)

        print("Préstamo realizado correctamente.")

    def devolver_libro(self):

        id_usuario = int(input("ID del usuario: "))
        id_libro = int(input("ID del libro: "))

        for usuario in self.usuarios:

            if usuario.id == id_usuario:

                if id_libro in usuario.libros_prestados:

                    usuario.libros_prestados.remove(id_libro)

                    for libro in self.libros:
                        if libro.id == id_libro:
                            libro.disponible = True

                    print("Libro devuelto.")
                    return

        print("No fue posible devolver el libro.")


    def guardar_datos(self):

        datos_libros = []

        for libro in self.libros:
            datos_libros.append({
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
                datos_libros,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        datos_usuarios = []

        for usuario in self.usuarios:
            datos_usuarios.append({
                "id": usuario.id,
                "nombre": usuario.nombre,
                "libros_prestados": usuario.libros_prestados,
                "total_prestamos": usuario.total_prestamos
            })

        with open(
            "usuarios.json",
            "w",
            encoding="utf-8"
        ) as archivo:
            json.dump(
                datos_usuarios,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        with open(
            "prestamos.json",
            "w",
            encoding="utf-8"
        ) as archivo:
            json.dump(
                self.historial,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def cargar_datos(self):

        try:
            with open(
                "libros.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                for d in datos:

                    libro = Libro(
                        d["id"],
                        d["titulo"],
                        d["autor"],
                        d["categoria"],
                        d["seccion"]
                    )

                    libro.disponible = d["disponible"]
                    libro.veces_prestado = d["veces_prestado"]

                    self.libros.append(libro)

        except:
            pass

        try:
            with open(
                "usuarios.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                for d in datos:

                    usuario = Usuario(
                        d["id"],
                        d["nombre"]
                    )

                    usuario.libros_prestados = d["libros_prestados"]
                    usuario.total_prestamos = d["total_prestamos"]

                    self.usuarios.append(usuario)

        except:
            pass

        try:
            with open(
                "prestamos.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                self.historial = json.load(archivo)

        except:
            pass

    def ordenar_por_titulo(self):

        libros_ordenados = sorted(
            self.libros,
            key=lambda libro: libro.titulo
        )

        for libro in libros_ordenados:
            print(libro.titulo)

    def ordenar_por_autor(self):

        libros_ordenados = sorted(
            self.libros,
            key=lambda libro: libro.autor
        )

        for libro in libros_ordenados:
            print(libro.autor, "-", libro.titulo)

    def ordenar_por_prestamos(self):

        libros_ordenados = sorted(
            self.libros,
            key=lambda libro: libro.veces_prestado,
            reverse=True
        )

        for libro in libros_ordenados:
            print(
                libro.titulo,
                "-",
                libro.veces_prestado,
                "préstamos"
            )

    def libro_mas_prestado(self):

        if len(self.libros) == 0:
            return

        mayor = self.libros[0]

        for libro in self.libros:

            if libro.veces_prestado > mayor.veces_prestado:
                mayor = libro

        print(
            "Libro más prestado:",
            mayor.titulo
        )

    def usuario_mas_activo(self):

        if len(self.usuarios) == 0:
            return

        mayor = self.usuarios[0]

        for usuario in self.usuarios:

            if usuario.total_prestamos > mayor.total_prestamos:
                mayor = usuario

        print(
            "Usuario con más préstamos:",
            mayor.nombre
        )

    def buscar_ruta(
        self,
        inicio,
        destino,
        visitados=[]
    ):

        visitados = visitados + [inicio]

        if inicio == destino:
            return visitados

        for vecino in self.grafo[inicio]:

            if vecino not in visitados:

                ruta = self.buscar_ruta(
                    vecino,
                    destino,
                    visitados
                )

                if ruta:
                    return ruta

        return None

    def encontrar_libro(self):

        titulo = input(
            "Título del libro: "
        )

        for libro in self.libros:

            if libro.titulo.lower() == titulo.lower():

                ruta = self.buscar_ruta(
                    "Entrada",
                    libro.seccion
                )
         
            if ruta:
                print("Ruta:"," -> ".join(ruta) )
            else:
                print("No se encontró la ruta.")
                return

        print("Libro no encontrado.")


# =========================
# MENÚ PRINCIPAL
# =========================

biblioteca = Biblioteca()

while True:

    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Agregar un libro")
    print("2. Mostrar un libros")
    print("3. Buscar um libro")
    print("4. Cambiar disponibilidad")
    print("5. Registrar al usuario")
    print("6. Prestar un libro")
    print("7. Devolver el libro")
    print("8. Ordenar por título")
    print("9. Ordenar por autor")
    print("10. Ordenar por préstamos")
    print("11. Libros más prestados")
    print("12. Usuario con más préstamos")
    print("13. Buscar ruta de un libro")
    print("14. Guardar y salir")

    opcion = input("Seleccionar una opción: ")

    if opcion == "1":
        biblioteca.agregar_libro()

    elif opcion == "2":
        biblioteca.mostrar_libros()

    elif opcion == "3":
        biblioteca.buscar_libro()

    elif opcion == "4":
        biblioteca.cambiar_disponibilidad()

    elif opcion == "5":
        biblioteca.agregar_usuario()

    elif opcion == "6":
        biblioteca.prestar_libro()

    elif opcion == "7":
        biblioteca.devolver_libro()

    elif opcion == "8":
        biblioteca.ordenar_por_titulo()

    elif opcion == "9":
        biblioteca.ordenar_por_autor()

    elif opcion == "10":
        biblioteca.ordenar_por_prestamos()

    elif opcion == "11":
        biblioteca.libro_mas_prestado()

    elif opcion == "12":
        biblioteca.usuario_mas_activo()

    elif opcion == "13":
        biblioteca.encontrar_libro()

    elif opcion == "14":
        biblioteca.guardar_datos()
        print("Datos guardados. Programa finalizado.")
        break

    else:
        print("Opción inválida.")
        