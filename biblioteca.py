class Biblioteca:
    """
    Clase que gestiona usuarios y recursos.
    """
    def __init__(self):
        self.recursos = []
        self.usuarios = []

    def agregar_recurso(self, recurso):
        self.recursos.append(recurso)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_por_titulo(self, titulo):
        resultados = []
        for recurso in self.recursos:
            if titulo.lower() in recurso.titulo.lower():
                resultados.append(recurso)
        return resultados

    def buscar_usuario_por_id(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def buscar_recurso_exacto(self, titulo_recurso):
        for recurso in self.recursos:
            if recurso.titulo.lower() == titulo_recurso.lower():
                return recurso
        return None

    def realizar_prestamo(self, id_usuario, titulo_recurso):
        try:
            usuario = self.buscar_usuario_por_id(id_usuario)
            if usuario is None:
                raise Exception(f"No existe un usuario con ID {id_usuario}.")

            recurso = self.buscar_recurso_exacto(titulo_recurso)
            if recurso is None:
                raise Exception(f"No existe el recurso '{titulo_recurso}'.")

            recurso.prestar(usuario)
            print(f"Préstamo realizado: {recurso.titulo} para {usuario.nombre}.")

        except Exception as error:
            print(f"Error en el préstamo: {error}")

    def realizar_devolucion(self, titulo_recurso):
        try:
            recurso = self.buscar_recurso_exacto(titulo_recurso)
            if recurso is None:
                raise Exception(f"No existe el recurso '{titulo_recurso}'.")

            recurso.devolver()
            print(f"Devolución realizada: {recurso.titulo}.")

        except Exception as error:
            print(f"Error en la devolución: {error}")

    def buscar_disponibles_por_genero(self, genero):
        return list(
            filter(
                lambda recurso: recurso.genero.lower() == genero.lower() and recurso.disponible,
                self.recursos
            )
        )

    def generar_informe_general(self):
        for recurso in self.recursos:
            yield str(recurso)
            