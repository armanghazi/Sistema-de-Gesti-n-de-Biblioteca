from recurso import Recurso


class Revista(Recurso):
    """
    Subclase para revistas.
    """
    def __init__(self, titulo, genero, numero_edicion):
        super().__init__(titulo, genero, duracion_prestamo=7)
        self.numero_edicion = numero_edicion

    def __str__(self):
        return (
            f"{super().__str__()} | Tipo: Revista | "
            f"Edición: {self.numero_edicion} | "
            f"Duración préstamo: {self.duracion_prestamo} días"
        )
    