class Usuario:
    """
    Representa a un usuario de la biblioteca.
    """
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario
        self.prestamos_activos = []

    def mostrar_prestamos(self):
        if not self.prestamos_activos:
            print(f"{self.nombre} no tiene préstamos activos.")
        else:
            print(f"Préstamos activos de {self.nombre} {self.apellido}:")
            for recurso in self.prestamos_activos:
                print(f"- {recurso.titulo}")

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido} | ID: {self.id_usuario}"