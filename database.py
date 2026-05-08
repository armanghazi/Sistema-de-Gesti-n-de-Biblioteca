import sqlite3
from datetime import datetime
from usuario import Usuario
from modelos.libro import Libro
from modelos.revista import Revista
from modelos.dvd import DVD

DB_PATH = "biblioteca.db"


def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = _get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS recursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            disponible INTEGER NOT NULL DEFAULT 1,
            prestado_a_id INTEGER,
            duracion_prestamo INTEGER NOT NULL DEFAULT 3,
            isbn TEXT,
            num_paginas INTEGER,
            numero_edicion TEXT,
            duracion_minutos INTEGER,
            FOREIGN KEY (prestado_a_id) REFERENCES usuarios(id)
        );

        CREATE TABLE IF NOT EXISTS prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            id_recurso INTEGER NOT NULL,
            fecha_prestamo TEXT NOT NULL,
            fecha_devolucion TEXT,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
            FOREIGN KEY (id_recurso) REFERENCES recursos(id)
        );
    """)
    conn.commit()
    conn.close()


def guardar_usuario(usuario):
    conn = _get_conn()
    conn.execute(
        "INSERT OR REPLACE INTO usuarios (id, nombre, apellido) VALUES (?, ?, ?)",
        (usuario.id_usuario, usuario.nombre, usuario.apellido)
    )
    conn.commit()
    conn.close()


def cargar_usuarios():
    conn = _get_conn()
    filas = conn.execute("SELECT * FROM usuarios").fetchall()
    usuarios = [Usuario(f["nombre"], f["apellido"], f["id"]) for f in filas]
    conn.close()
    return usuarios


def guardar_recurso(recurso):
    conn = _get_conn()
    tipo = recurso.__class__.__name__
    isbn = getattr(recurso, "isbn", None)
    num_paginas = getattr(recurso, "num_paginas", None)
    numero_edicion = getattr(recurso, "numero_edicion", None)
    duracion_minutos = getattr(recurso, "duracion_minutos", None)
    prestado_a_id = recurso.prestado_a.id_usuario if recurso.prestado_a else None

    if recurso.id is None:
        cursor = conn.execute(
            """INSERT INTO recursos
               (tipo, titulo, genero, disponible, prestado_a_id, duracion_prestamo,
                isbn, num_paginas, numero_edicion, duracion_minutos)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (tipo, recurso.titulo, recurso.genero, int(recurso.disponible),
             prestado_a_id, recurso.duracion_prestamo,
             isbn, num_paginas, numero_edicion, duracion_minutos)
        )
        recurso.id = cursor.lastrowid
    else:
        conn.execute(
            """UPDATE recursos SET tipo=?, titulo=?, genero=?, disponible=?,
               prestado_a_id=?, duracion_prestamo=?, isbn=?, num_paginas=?,
               numero_edicion=?, duracion_minutos=? WHERE id=?""",
            (tipo, recurso.titulo, recurso.genero, int(recurso.disponible),
             prestado_a_id, recurso.duracion_prestamo,
             isbn, num_paginas, numero_edicion, duracion_minutos, recurso.id)
        )
    conn.commit()
    conn.close()


def cargar_recursos():
    usuarios = cargar_usuarios()
    usuarios_map = {u.id_usuario: u for u in usuarios}

    conn = _get_conn()
    filas = conn.execute("SELECT * FROM recursos").fetchall()
    recursos = []
    for f in filas:
        tipo = f["tipo"]
        if tipo == "Libro":
            r = Libro(f["titulo"], f["genero"], f["isbn"], f["num_paginas"])
        elif tipo == "Revista":
            r = Revista(f["titulo"], f["genero"], f["numero_edicion"])
        elif tipo == "DVD":
            r = DVD(f["titulo"], f["genero"], f["duracion_minutos"])
        else:
            continue

        r.id = f["id"]
        r.disponible = bool(f["disponible"])
        r.duracion_prestamo = f["duracion_prestamo"]
        if f["prestado_a_id"] and f["prestado_a_id"] in usuarios_map:
            r.prestado_a = usuarios_map[f["prestado_a_id"]]
        recursos.append(r)

    conn.close()

    for r in recursos:
        if r.prestado_a and r not in r.prestado_a.prestamos_activos:
            r.prestado_a.prestamos_activos.append(r)

    return recursos


def actualizar_estado_recurso(recurso):
    conn = _get_conn()
    prestado_a_id = recurso.prestado_a.id_usuario if recurso.prestado_a else None
    conn.execute(
        "UPDATE recursos SET disponible = ?, prestado_a_id = ? WHERE id = ?",
        (int(recurso.disponible), prestado_a_id, recurso.id)
    )
    conn.commit()
    conn.close()


def registrar_prestamo_db(id_usuario, id_recurso):
    conn = _get_conn()
    conn.execute(
        "INSERT INTO prestamos (id_usuario, id_recurso, fecha_prestamo) VALUES (?, ?, ?)",
        (id_usuario, id_recurso, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def registrar_devolucion_db(id_recurso):
    conn = _get_conn()
    conn.execute(
        "UPDATE prestamos SET fecha_devolucion = ? "
        "WHERE id_recurso = ? AND fecha_devolucion IS NULL",
        (datetime.now().isoformat(), id_recurso)
    )
    conn.commit()
    conn.close()
