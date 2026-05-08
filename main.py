import questionary

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import IntPrompt

console = Console()


def mostrar_menu():
    console.print(
        Panel.fit(
            "[bold cyan]SISTEMA DE BIBLIOTECA[/bold cyan]",
            border_style="blue"
        )
    )

    return questionary.select(
        "Selecciona una opción:",
        choices=[
            "➕ Agregar nuevo material",
            "📚 Listar materiales",
            "🔍 Mostrar detalle",
            "❌ Salir"
        ]
    ).ask()


def agregar_material(biblioteca):

    opcion = questionary.select(
        "¿Qué tipo de material quieres agregar?",
        choices=[
            "📖 Libro",
            "📰 Revista",
            "🎬 DVD"
        ]
    ).ask()

    titulo = questionary.text("Título:").ask()
    genero = questionary.text("Género:").ask()

    try:

        if "Libro" in opcion:

            isbn = questionary.text("ISBN:").ask()

            num_paginas = IntPrompt.ask(
                "[cyan]Número de páginas[/cyan]"
            )

            recurso = Libro(
                titulo,
                genero,
                isbn,
                num_paginas
            )

            biblioteca.agregar_recurso(recurso)

            console.print(
                "[bold green]✓ Libro agregado correctamente[/bold green]"
            )

        elif "Revista" in opcion:

            numero_edicion = questionary.text(
                "Número de edición:"
            ).ask()

            recurso = Revista(
                titulo,
                genero,
                numero_edicion
            )

            biblioteca.agregar_recurso(recurso)

            console.print(
                "[bold green]✓ Revista agregada correctamente[/bold green]"
            )

        elif "DVD" in opcion:

            duracion = IntPrompt.ask(
                "[cyan]Duración en minutos[/cyan]"
            )

            recurso = DVD(
                titulo,
                genero,
                duracion
            )

            biblioteca.agregar_recurso(recurso)

            console.print(
                "[bold green]✓ DVD agregado correctamente[/bold green]"
            )

    except ValueError:

        console.print(
            "[bold red]✗ Error: valor inválido[/bold red]"
        )


def listar_materiales(biblioteca):

    console.print("\n")

    if not biblioteca.recursos:

        console.print(
            Panel(
                "[yellow]No hay materiales registrados[/yellow]",
                title="Biblioteca"
            )
        )

        return

    table = Table(
        title="📚 Lista de Materiales",
        show_lines=True
    )

    table.add_column("Título", style="cyan")
    table.add_column("Género", style="green")
    table.add_column("Tipo", style="magenta")

    for recurso in biblioteca.recursos:

        table.add_row(
            recurso.titulo,
            recurso.genero,
            recurso.__class__.__name__
        )

    console.print(table)


def mostrar_detalle_material(biblioteca):

    titulo = questionary.text(
        "Introduce el título:"
    ).ask()

    recurso = biblioteca.buscar_recurso_exacto(titulo)

    if recurso is None:

        console.print(
            "[bold red]No se encontró el material[/bold red]"
        )

    else:

        console.print(
            Panel(
                str(recurso),
                title="📖 Información detallada",
                border_style="green"
            )
        )


def main():

    biblioteca = biblioteca()

    # Usuarios
    usuario1 = Usuario("Ana", "García", 1)
    usuario2 = Usuario("Carlos", "López", 2)

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Recursos iniciales
    libro1 = Libro(
        "El Hobbit",
        "Fantasía",
        "978-84-450-7370-7",
        310
    )

    revista1 = Revista(
        "National Geographic",
        "Ciencia",
        125
    )

    dvd1 = DVD(
        "Interestelar",
        "Ciencia Ficción",
        169
    )

    biblioteca.agregar_recurso(libro1)
    biblioteca.agregar_recurso(revista1)
    biblioteca.agregar_recurso(dvd1)

    while True:

        opcion = mostrar_menu()

        if "Agregar" in opcion:

            agregar_material(biblioteca)

        elif "Listar" in opcion:

            listar_materiales(biblioteca)

        elif "Mostrar" in opcion:

            mostrar_detalle_material(biblioteca)

        elif "Salir" in opcion:

            console.print(
                "\n[bold blue]👋 Hasta luego[/bold blue]"
            )

            break


if __name__ == "__main__":
    main()