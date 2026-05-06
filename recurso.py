from datetime import datetime
from functools import wraps


def registrar_accion(funcion):
    """
    Decorador que registra en el archivo de log
    las acciones de préstamo y devolución.
    """
    @wraps(funcion)
    def envoltura(self, *args, **kwargs):
        resultado = funcion(self, *args, **kwargs)

        with open("biblioteca_log.txt", "a", encoding="utf-8") as archivo:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(
                f"{fecha_hora} | Operación: {funcion.__name__} | "
                f"Recurso: {self.titulo}\n"
            )

        return resultado

    return envoltura


class Recurso:
    """
    Clase base para cualquier recurso de la biblioteca.
    """
    def __init__(self, titulo, genero, duracion_prestamo=3):
        self.titulo = titulo
        self.genero = genero
        self.disponible = True
        self.prestado_a = None
        self.duracion_prestamo = duracion_prestamo

    def __str__(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = f"Prestado a {self.prestado_a.nombre}"
        return f"{self.titulo} ({self.genero}) - {estado}"

    @registrar_accion
    def prestar(self, usuario):
        if not self.disponible:
            raise Exception(f"El recurso '{self.titulo}' no está disponible.")

        self.disponible = False
        self.prestado_a = usuario
        usuario.prestamos_activos.append(self)

    @registrar_accion
    def devolver(self):
        if self.disponible:
            raise Exception(f"El recurso '{self.titulo}' no estaba prestado.")

        if self in self.prestado_a.prestamos_activos:
            self.prestado_a.prestamos_activos.remove(self)

        self.disponible = True
        self.prestado_a = None