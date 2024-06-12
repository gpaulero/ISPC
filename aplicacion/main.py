from menu import mostrar_menu
import tareas

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = int(input("Ingrese la prioridad de la tarea (1-5): "))
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (AAAA-MM-DD): ")
            categoria_id = int(input("Ingrese el ID de la categoría: "))
            tareas.crear_tarea(nombre, descripcion, prioridad, fecha_vencimiento, categoria_id)
            print("Tarea creada con éxito.")
        elif opcion == "2":
            todas_tareas = tareas.ver_tareas()
            for tarea in todas_tareas:
                print(tarea)
        elif opcion == "3":
            id = int(input("Ingrese el ID de la tarea a editar: "))
            nombre = input("Ingrese el nuevo nombre de la tarea: ")
            descripcion = input("Ingrese la nueva descripción de la tarea: ")
            prioridad = int(input("Ingrese la nueva prioridad de la tarea (1-5): "))
            fecha_vencimiento = input("Ingrese la nueva fecha de vencimiento (AAAA-MM-DD): ")
            categoria_id = int(input("Ingrese el nuevo ID de la categoría: "))
            tareas.editar_tarea(id, nombre, descripcion, prioridad, fecha_vencimiento, categoria_id)
            print("Tarea editada con éxito.")
        elif opcion == "4":
            id = int(input("Ingrese el ID de la tarea a eliminar: "))
            tareas.eliminar_tarea(id)
            print("Tarea eliminada con éxito.")
        elif opcion == "5":
            print("Gracias por usar el Gestor de Tareas Personales.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
