from recurso import Recurso


class Libro(Recurso):
    """
    Subclase para libros.
    """
    def __init__(self, titulo, genero, isbn, num_paginas):
        super().__init__(titulo, genero, duracion_prestamo=3)
        self.isbn = isbn
        self.num_paginas = num_paginas

    def __str__(self):
        return (
            f"{super().__str__()} | Tipo: Libro | "
            f"ISBN: {self.isbn} | Páginas: {self.num_paginas} | "
            f"Duración préstamo: {self.duracion_prestamo} días"
        )