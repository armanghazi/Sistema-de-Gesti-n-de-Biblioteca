from usuario import Usuario
from biblioteca import Biblioteca
from modelos.libro import Libro
from modelos.revista import Revista
from modelos.dvd import DVD


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

    # Agregar recursos
    biblioteca.agregar_recurso(libro1)
    biblioteca.agregar_recurso(revista1)
    biblioteca.agregar_recurso(dvd1)

    # Buscar por título
    print("Búsqueda por título:")
    for recurso in biblioteca.buscar_por_titulo("el"):
        print(recurso)

    print()

    # Realizar préstamo
    biblioteca.realizar_prestamo(1, "El Hobbit")
    biblioteca.realizar_prestamo(2, "El Hobbit")

    print()

    # Mostrar préstamos
    usuario1.mostrar_prestamos()

    print()

    # Buscar disponibles por género
    print("Recursos disponibles del género Ciencia:")
    for recurso in biblioteca.buscar_disponibles_por_genero("Ciencia"):
        print(recurso)

    print()

    # Devolver recurso
    biblioteca.realizar_devolucion("El Hobbit")

    print()

    # Informe general
    print("Informe general:")
    for linea in biblioteca.generar_informe_general():
        print(linea)


if __name__ == "__main__":
    main()
