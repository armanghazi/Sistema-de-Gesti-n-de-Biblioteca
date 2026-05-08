# AGENTS.md — Sistema de Gestión de Biblioteca

## Entrypoints

- **`main.py`** — interactive CLI app. Requires `questionary` + `rich` (see `pip list`).
- **`main0.py`** — script-based demo using only stdlib. Preferred for quick smoke tests.

## Known bugs in `main.py`

- `biblioteca = biblioteca()` on line 172 shadows the module — should be `Biblioteca()`.
- Classes `Libro`, `Revista`, `DVD`, `Usuario` are used but never imported at the top of the file.

## Import convention

`modelos/*.py` use flat imports: `from recurso import Recurso` — they are NOT relative (`from ..recurso`). This works because the package is flat (no `__init__.py`-level namespace wrapping). Keep this style if adding new model subclasses.

## Runtime artifact

`biblioteca_log.txt` is generated automatically by the `@registrar_accion` decorator in `recurso.py` on `prestar`/`devolver` calls. It is git-ignored or should be.

## No tests / No linting / No CI

This is a minimal educational repo. There is no test suite, no linter config, no type checker, no CI pipeline.
Run `python main0.py` to verify changes manually.

## Dependencies

- `questionary` — interactive prompts (used only in `main.py`)
- `rich` — terminal formatting (used only in `main.py`)
- Otherwise stdlib-only (Python 3.13).

## Architecture

```
biblioteca.py   → Biblioteca class (orchestrator)
recurso.py      → Recurso base class + @registrar_accion decorator
usuario.py      → Usuario class
modelos/        → Subclasses: Libro, Revista, DVD (each extends Recurso)
```
