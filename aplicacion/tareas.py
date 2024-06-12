from bd import conectar

def crear_tarea(nombre, descripcion, prioridad, fecha_vencimiento, categoria_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO tareas (nombre, descripcion, prioridad, fecha_vencimiento, categoria_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (nombre, descripcion, prioridad, fecha_vencimiento, categoria_id))

    conexion.commit()
    cursor.close()
    conexion.close()

def ver_tareas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()

    cursor.close()
    conexion.close()
    return tareas

def editar_tarea(id, nombre, descripcion, prioridad, fecha_vencimiento, categoria_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE tareas
        SET nombre=%s, descripcion=%s, prioridad=%s, fecha_vencimiento=%s, categoria_id=%s
        WHERE id=%s
    """, (nombre, descripcion, prioridad, fecha_vencimiento, categoria_id, id))

    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_tarea(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM tareas WHERE id=%s", (id,))

    conexion.commit()
    cursor.close()
    conexion.close()
