from usuario import Usuario
from biblioteca import Biblioteca
from modelos.libro import Libro
from modelos.revista import Revista
from modelos.dvd import DVD


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar nuevo material")
    print("2. Listar todos los materiales")
    print("3. Mostrar información de un material")
    print("4. Salir")


def agregar_material(biblioteca):
    print("\n¿Qué tipo de material quieres agregar?")
    print("1. Libro")
    print("2. Revista")
    print("3. DVD")

    opcion = input("Selecciona una opción: ")

    titulo = input("Título: ")
    genero = input("Género: ")

    try:
        if opcion == "1":
            isbn = input("ISBN: ")
            num_paginas = int(input("Número de páginas: "))
            recurso = Libro(titulo, genero, isbn, num_paginas)
            biblioteca.agregar_recurso(recurso)
            print("Libro agregado correctamente.")

        elif opcion == "2":
            numero_edicion = input("Número de edición: ")
            recurso = Revista(titulo, genero, numero_edicion)
            biblioteca.agregar_recurso(recurso)
            print("Revista agregada correctamente.")

        elif opcion == "3":
            duracion_minutos = int(input("Duración en minutos: "))
            recurso = DVD(titulo, genero, duracion_minutos)
            biblioteca.agregar_recurso(recurso)
            print("DVD agregado correctamente.")

        else:
            print("Opción no válida.")

    except ValueError:
        print("Error: debes introducir un número válido.")


def listar_materiales(biblioteca):
    print("\n--- LISTA DE MATERIALES ---")
    if not biblioteca.recursos:
        print("No hay materiales registrados.")
    else:
        for recurso in biblioteca.recursos:
            print(recurso)


def mostrar_detalle_material(biblioteca):
    titulo = input("\nIntroduce el título del material: ")
    recurso = biblioteca.buscar_recurso_exacto(titulo)

    if recurso is None:
        print("No se encontró ese material.")
    else:
        print("\n--- INFORMACIÓN DETALLADA ---")
        print(recurso)


def main():
    biblioteca = Biblioteca()

    # Crear usuarios
    usuario1 = Usuario("Ana", "García", 1)
    usuario2 = Usuario("Carlos", "López", 2)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Crear recursos
    libro1 = Libro("El Hobbit", "Fantasía", "978-84-450-7370-7", 310)
    revista1 = Revista("National Geographic", "Ciencia", 125)
    dvd1 = DVD("Interestelar", "Ciencia Ficción", 169)

    # Agregar recursos iniciales
    biblioteca.agregar_recurso(libro1)
    biblioteca.agregar_recurso(revista1)
    biblioteca.agregar_recurso(dvd1)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_material(biblioteca)

        elif opcion == "2":
            listar_materiales(biblioteca)

        elif opcion == "3":
            mostrar_detalle_material(biblioteca)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()



