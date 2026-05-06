# Sistema de Gestión de Biblioteca

Proyecto de práctica de Programación Orientada a Objetos (POO) en Python, organizado en varios archivos para separar responsabilidades y facilitar el mantenimiento del código. Esta estructura permite trabajar de forma clara con encapsulamiento, composición, herencia y una clase gestora central, tal como plantea el ejercicio. [file:1]

## Objetivo

El proyecto simula una biblioteca donde se pueden registrar usuarios, agregar recursos, realizar préstamos y devoluciones, buscar materiales por título o género y generar un informe general. También incorpora un archivo de log para registrar automáticamente las acciones realizadas sobre los recursos. [file:1]

## Estructura del proyecto

```text
biblioteca/
│
├── recurso.py
├── usuario.py
├── biblioteca.py
├── main.py
└── modelos/
   ├── __init__.py
   ├── libro.py
   ├── revista.py
   └── dvd.py
```

## Descripción de los archivos

### `recurso.py`

Contiene la clase base `Recurso`, que representa cualquier material bibliotecario. Incluye los atributos comunes (`titulo`, `genero`, `disponible`, `prestado_a`, `duracion_prestamo`) y los métodos `prestar()` y `devolver()`, además del decorador que registra cada acción en `biblioteca_log.txt`. [file:1]

### `usuario.py`

Contiene la clase `Usuario`, con los atributos `nombre`, `id_usuario` y `prestamos_activos`. Esta clase permite representar al usuario como objeto, lo que da soporte a la composición entre `Usuario` y `Recurso`. [file:1]

### `modelos/libro.py`

Define la clase `Libro`, que hereda de `Recurso` y añade atributos propios como `isbn` y `num_paginas`. La duración del préstamo para libros es de 3 días. [file:1]

### `modelos/revista.py`

Define la clase `Revista`, que hereda de `Recurso` y añade el atributo `numero_edicion`. La duración del préstamo para revistas es de 7 días. [file:1]

### `modelos/dvd.py`

Define la clase `DVD`, que hereda de `Recurso` y añade el atributo `duracion_minutos`. La duración del préstamo para DVDs es de 2 días. [file:1]

### `biblioteca.py`

Contiene la clase `Biblioteca`, que actúa como gestor central del sistema. Administra la lista de recursos y usuarios, permite buscar por título, realizar préstamos seguros con `try...except`, buscar recursos disponibles por género usando `filter` y `lambda`, y generar un informe general mediante `yield`. [file:1]

### `main.py`

Es el archivo principal para probar el funcionamiento del sistema. Aquí se crean usuarios y recursos, se registran préstamos y devoluciones, y se muestran búsquedas e informes. [file:1]

## Funcionalidades principales

- Crear recursos bibliotecarios a partir de una clase base. [file:1]
- Crear usuarios con una lista de préstamos activos. [file:1]
- Aplicar herencia con las clases `Libro`, `Revista` y `DVD`. [file:1]
- Gestionar préstamos y devoluciones con validaciones. [file:1]
- Registrar acciones automáticamente en `biblioteca_log.txt`. [file:1]
- Buscar recursos por título. [file:1]
- Filtrar recursos disponibles por género con `filter` y `lambda`. [file:1]
- Generar un informe general usando `yield`. [file:1]

## Requisitos

- Python 3.x
- No se necesitan librerías externas, ya que el proyecto usa módulos estándar como `datetime` y `functools`.

## Cómo ejecutar el proyecto

1. Guardar todos los archivos dentro de la carpeta `biblioteca` con la estructura indicada.  
2. Abrir una terminal en esa carpeta.  
3. Ejecutar el archivo principal con:

```bash
python main.py
```

## Ejemplo de uso

El archivo `main.py` puede incluir pruebas como estas:

```python
from usuario import Usuario
from biblioteca import Biblioteca
from modelos.libro import Libro
from modelos.revista import Revista
from modelos.dvd import DVD

biblioteca = Biblioteca()

usuario1 = Usuario("Ana García", 1)
biblioteca.registrar_usuario(usuario1)

libro1 = Libro("El Hobbit", "Fantasía", "978-84-450-7370-7", 310)
biblioteca.agregar_recurso(libro1)

biblioteca.realizar_prestamo(1, "El Hobbit")
usuario1.mostrar_prestamos()
```

## Archivo de log

Cada vez que se presta o devuelve un recurso, se escribe una línea en `biblioteca_log.txt` con la fecha, la hora, el tipo de operación y el título del recurso afectado. Esto responde directamente al requisito del ejercicio de registrar automáticamente la actividad del sistema. [file:1]

## Conceptos de POO aplicados

- **Encapsulamiento**: cada clase organiza sus propios atributos y métodos. [file:1]
- **Composición**: un recurso prestado guarda una referencia a un objeto `Usuario`. [file:1]
- **Herencia**: `Libro`, `Revista` y `DVD` heredan de `Recurso`. [file:1]
- **Polimorfismo básico**: cada subclase personaliza su representación con `__str__()`. [file:1]
- **Gestión centralizada**: la clase `Biblioteca` coordina usuarios y recursos. [file:1]

## Observaciones

Esta organización modular no siempre es obligatoria en ejercicios pequeños, pero mejora mucho la claridad del proyecto y hace que la solución se vea más profesional. Además, ayuda a explicar mejor cada fase del ejercicio por separado. [file:1]
