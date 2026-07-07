from biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:

    print("\n===== BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Registrar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Libro más prestado")
    print("8. Usuario más activo")
    print("9. Buscar ruta de un libro")
    print("10. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        biblioteca.agregar_libro()

    elif opcion == "2":
        biblioteca.mostrar_libros()

    elif opcion == "3":
        biblioteca.buscar_libro()

    elif opcion == "4":
        biblioteca.agregar_usuario()

    elif opcion == "5":
        biblioteca.prestar_libro()

    elif opcion == "6":
        biblioteca.devolver_libro()

    elif opcion == "7":
        biblioteca.libro_mas_prestado()

    elif opcion == "8":
        biblioteca.usuario_mas_activo()

    elif opcion == "9":
        biblioteca.encontrar_libro()

    elif opcion == "10":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")