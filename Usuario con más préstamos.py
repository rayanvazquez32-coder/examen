    def usuario_mas_activo(self):

        if len(self.usuarios) == 0:
            return

        mayor = self.usuarios[0]

        for usuario in self.usuarios:

            if usuario.total_prestamos > mayor.total_prestamos:
                mayor = usuario

        print("Usuario con más préstamos:")
        print(mayor.nombre)