    def agregar_usuario(self):

        id = int(input("ID del usuario: "))
        nombre = input("Nombre: ")

        usuario = Usuario(id, nombre)

        self.usuarios.append(usuario)

        print("Usuario registrado.")