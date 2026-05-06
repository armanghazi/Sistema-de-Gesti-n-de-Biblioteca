from recurso import Recurso


class DVD(Recurso):
    """
    Subclase para DVDs.
    """
    def __init__(self, titulo, genero, duracion_minutos):
        super().__init__(titulo, genero, duracion_prestamo=2)
        self.duracion_minutos = duracion_minutos

    def __str__(self):
        return (
            f"{super().__str__()} | Tipo: DVD | "
            f"Duración: {self.duracion_minutos} min | "
            f"Duración préstamo: {self.duracion_prestamo} días"
        )
    