# menu.py

from tareas import crear_tarea, ver_tareas, editar_tarea, eliminar_tarea

def mostrar_menu_principal():
    print("\n=== Menú Principal ===")
    print("1. Crear una nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Editar una tarea")
    print("4. Eliminar una tarea")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        editar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Gracias por usar el Gestor de Tareas Personales")
        exit()
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
