# main.py
import mysql.connector
from config import db_config

def conectar():
    return mysql.connector.connect(**db_config)

def crear_tarea(nombre, descripcion, prioridad, fecha_vencimiento, categoria_id):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO tareas (nombre, descripcion, prioridad, fecha_vencimiento, categoria_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, descripcion, prioridad, fecha_vencimiento, categoria_id))
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_tareas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas")
    for tarea in cursor.fetchall():
        print(tarea)
    cursor.close()
    conexion.close()

def actualizar_tarea(id, nombre, descripcion, prioridad, fecha_vencimiento, categoria_id):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE tareas SET nombre=%s, descripcion=%s, prioridad=%s, fecha_vencimiento=%s, categoria_id=%s WHERE id=%s"
    cursor.execute(query, (nombre, descripcion, prioridad, fecha_vencimiento, categoria_id, id))
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

# main.py - menú principal
def menu():
    while True:
        print("1. Crear una nueva tarea")
        print("2. Ver todas las tareas")
        print("3. Editar una tarea")
        print("4. Eliminar una tarea")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Ejemplo de llamada a crear_tarea
            crear_tarea("Nueva Tarea", "Descripción de la tarea", 1, "2024-07-01", 1)
        elif opcion == '2':
            leer_tareas()
        elif opcion == '3':
            # Ejemplo de llamada a actualizar_tarea
            actualizar_tarea(1, "Tarea Actualizada", "Descripción actualizada", 2, "2024-07-10", 2)
        elif opcion == '4':
            # Ejemplo de llamada a eliminar_tarea
            eliminar_tarea(1)
        elif opcion == '5':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
