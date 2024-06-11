# ISPC

Detallar los datos de los integrantes del grupo: 

Nombre y apellido: Gonzalo Paulero

DNI: 35278960

Mail: gpaulero@gmail.com

Link: https://github.com/gpaulero/ISPC.git


# **Descripción de la propuesta de proyecto elegida:**

El Gestor de Tareas Personales es una aplicación diseñada para ayudar a los usuarios a organizar y gestionar sus tareas diarias de manera eficiente. 
Los usuarios podrán crear, editar y eliminar tareas, así como asignarles prioridades y fechas de vencimiento. 
La aplicación también permitirá la categorización de tareas y ofrecerá recordatorios para garantizar que los usuarios no olviden sus compromisos.

**Problema a Resolver**

El problema que se quiere resolver es la gestión eficiente de tareas personales. Muchas personas tienen dificultades para organizar y recordar sus tareas diarias, lo que puede llevar a olvidos y falta de productividad. La aplicación propuesta, Gestor de Tareas Personales, tiene como objetivo proporcionar una solución fácil de usar para organizar, priorizar y recordar las tareas pendientes.

**Análisis del Proyecto: Gestor de Tareas Personales**

**Objetivos del Proyecto**

Requisitos Funcionales

1- Organización Eficiente de Tareas:

- Proveer una herramienta que permita a los usuarios gestionar sus tareas de manera estructurada y eficiente.
- Facilitar la visualización y administración de todas las tareas de los usuarios en un solo lugar.

2- Gestión Completa de Tareas:

- Permitir la creación, visualización, edición y eliminación de tareas.
- Proveer una interfaz intuitiva para que los usuarios puedan realizar todas estas operaciones sin complicaciones.

3- Interfaz de Usuario Amigable:

- Ofrecer un menú principal claro y fácil de navegar, que guíe a los usuarios a través de las diferentes funcionalidades de la aplicación.
- Garantizar que la interacción con la aplicación sea sencilla y directa.

4- Experiencia de Usuario Mejorada:

- Asegurar que los usuarios reciban retroalimentación inmediata sobre las acciones realizadas (creación, edición, eliminación de tareas).
- Proporcionar mensajes de confirmación y agradecimiento para mejorar la satisfacción del usuario.

5- Consultas SQL:

- Consultas básicas para gestionar y filtrar tareas.
- Consultas avanzadas para buscar tareas por diferentes criterios (fecha, prioridad, etc.).

Alcance del Proyecto

1- Funcionalidades Básicas:

- Crear una Nueva Tarea: Los usuarios podrán ingresar detalles de nuevas tareas y agregarlas a su lista de tareas.
- Ver Todas las Tareas: La aplicación permitirá a los usuarios ver una lista de todas las tareas almacenadas.
- Editar una Tarea: Los usuarios podrán modificar los detalles de tareas existentes.
- Eliminación de Tareas: Se permitirá a los usuarios eliminar tareas que ya no sean relevantes o necesarias.

2- Interfaz de Usuario:

- Menú Principal: Un menú principal que presenta opciones claras para navegar entre las diferentes funcionalidades.
- Interacción Fluida: La aplicación guiará a los usuarios paso a paso para realizar cada operación (crear, ver, editar, eliminar tareas).

3- Mensajes y Retroalimentación:

- Mensajes de Bienvenida y Despedida: La aplicación mostrará mensajes amigables al iniciar y cerrar la sesión.
- Confirmaciones y Notificaciones: Se mostrarán confirmaciones después de cada operación para asegurar al usuario que la acción se ha completado exitosamente.

# **Estructura del Proyecto**

gestor_tareas/

│

├── main.py

├── tareas.py

├── usuarios.py

├── menu.py

**Descripción de los Archivos**
El proyecto está modularizado en varios archivos Python para mantener una estructura clara y organizada. A continuación se describen los archivos y su propósito:

### Archivos

1. **main.py**
   - Este es el archivo principal de la aplicación.
   - Contiene la función `main()` que inicia la aplicación y muestra el menú principal llamando a `mostrar_menu_principal()`.

2. **tareas.py**
   - Contiene las funciones relacionadas con la gestión de tareas.
   - Funciones:
     - `crear_tarea()`: Imprime un mensaje indicando que se ha seleccionado la opción de crear una tarea.
     - `ver_tareas()`: Imprime un mensaje indicando que se ha seleccionado la opción de ver todas las tareas.
     - `editar_tarea()`: Imprime un mensaje indicando que se ha seleccionado la opción de editar una tarea.
     - `eliminar_tarea()`: Imprime un mensaje indicando que se ha seleccionado la opción de eliminar una tarea.

3. **usuarios.py**
   - Contiene las funciones relacionadas con la gestión de usuarios.
   - Funciones:
     - `crear_usuario()`: Imprime un mensaje indicando que se ha seleccionado la opción de crear un usuario.
     - `ver_usuarios()`: Imprime un mensaje indicando que se ha seleccionado la opción de ver todos los usuarios.
     - `editar_usuario()`: Imprime un mensaje indicando que se ha seleccionado la opción de editar un usuario.
     - `eliminar_usuario()`: Imprime un mensaje indicando que se ha seleccionado la opción de eliminar un usuario.

4. **menu.py**
   - Contiene la lógica para mostrar el menú principal y manejar la navegación del usuario.
   - Llama a las funciones definidas en `tareas.py` y `usuarios.py`.

5. **bd.py**
   - Funciones para la conexión y operaciones con la base de datos.

# Aplicación

Para implementar la aplicación Gestor de Tareas Personales utilizando Python y una base de datos MySQL, seguiremos un enfoque modular. Este desarrollo incluirá el CRUD (Crear, Leer, Actualizar, Eliminar) de las tablas de la base de datos.

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

# main.py

from menu import mostrar_menu_principal

def main():

    print("Bienvenido al Gestor de Tareas Personales")
    while True:
        mostrar_menu_principal()

if __name__ == "__main__":

    main()


# tareas.py

from bd import ejecutar_consulta, obtener_datos


def crear_tarea():

    print("Opción seleccionada: Crear una nueva tarea")

def ver_tareas():

    print("Opción seleccionada: Ver todas las tareas")

def editar_tarea():

    print("Opción seleccionada: Editar una tarea")

def eliminar_tarea():

    print("Opción seleccionada: Eliminar una tarea")


# usuarios.py

from bd import ejecutar_consulta, obtener_datos

def crear_usuario():

    print("Opción seleccionada: Crear un nuevo usuario")

def ver_usuarios():

    print("Opción seleccionada: Ver todos los usuarios")

def editar_usuario():

    print("Opción seleccionada: Editar un usuario")

def eliminar_usuario():

    print("Opción seleccionada: Eliminar un usuario")

# bd.py

import mysql.connector

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="gestor_tareas"
    )

def ejecutar_consulta(query, params=None):

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

def obtener_datos(query, params=None):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados



# **Diagrama de Entidad-Relación (ERD)**
![Diagrama](https://github.com/gpaulero/ISPC/assets/169163764/2478ea6a-0f54-40ec-ab90-caf05bb0c8cc)
![diagrama crow's foot](https://github.com/gpaulero/ISPC/assets/169163764/1496f800-7e4f-4381-a69c-36eac20dab90)

**Entidades y Atributos**

1. Usuario

  - ID_Usuario (Clave primaria) (VARCHAR 45)
  - Nombre (VARCHAR 45)
  - Correo Electrónico (VARCHAR 45)

2. Tarea

  - ID_Tarea (Clave primaria) (VARCHAR 45)
  - Título (VARCHAR 45)
  - Descripción (VARCHAR 45)
  - Prioridad (VARCHAR 45)
  - Fecha de Vencimiento (DATE)
  - Categoría (VARCHAR 45)
  - ID_Usuario (Clave foránea) (VARCHAR 45)

3. Relaciones y Cardinalidades
  - Usuario - Tarea
  - Relación: "Posee"

**Cardinalidad:**

  Un Usuario puede poseer muchas Tareas (1).

  Una Tarea es poseída por un solo Usuario (N:1).

# **Descripción del Diagrama ER**

1- Entidad Usuario:

ID_Usuario: Un identificador único para cada usuario.
- Nombre: El nombre del usuario.
- Correo Electrónico: El correo electrónico del usuario.

2- Entidad Tarea:

- ID_Tarea: Un identificador único para cada tarea.
- Título: El título de la tarea.
- Descripción: La descripción detallada de la tarea.
- Prioridad: La prioridad asignada a la tarea (baja, media, alta).
- Fecha de Vencimiento: La fecha límite para completar la tarea.
- Categoría: La categoría a la que pertenece la tarea.
- ID_Usuario: El identificador del usuario que posee la tarea (clave foránea).
  

3- Relación Posee:

- Esta relación vincula al Usuario con la Tarea.
- La cardinalidad 1 indica que un usuario puede tener muchas tareas, pero cada tarea pertenece a un solo usuario.

# **Requisitos, pasos para su instalacion y uso.**

Para que una persona externa pueda entender y utilizar la aplicación "Gestor de Tareas Personales", debe proporcionar una descripción detallada del proyecto.

## Requisitos

### Software
- Python 3.x
- MySQL Server

### Librerías Python
- `mysql-connector-python

# **Instalar Dependencias**

pip install -r requirements.txt


##Configurar la Base de Datos##

Iniciar MySQL Server.

Crear la base de datos:
- Ejecutar el script de estructura de base de datos
- Ejecutar el script de inserción de datos:

# **Uso de la Aplicación**

- Menú Principal

- Crear una nueva tarea

- Ver todas las tareas

- Editar una tarea

- Eliminar una tarea

- Salir

**Funcionalidades**

Crear tarea: Permite al usuario agregar una nueva tarea con detalles como nombre, prioridad y fecha de vencimiento.

Ver tareas: Muestra una lista de todas las tareas guardadas en la base de datos.

Editar tarea: Permite modificar los detalles de una tarea existente.

Eliminar tarea: Elimina una tarea seleccionada de la base de datos.

Salir: Cierra la aplicación.


**Documentación**

ER Diagram: [Diagrama.png](https://github.com/gpaulero/ISPC/blob/main/Diagrama.png)

Crow Foot Diagram: [Diagrama crow's foot.png](https://github.com/gpaulero/ISPC/blob/main/diagrama%20crow's%20foot.png)

**Contribución**

Si deseas contribuir a este proyecto, por favor, sigue estos pasos:

- Haz un fork del proyecto.

- Crea una nueva rama (git checkout -b nueva-rama).

- Realiza tus cambios y haz commit (git commit -m 'Añadir nueva característica').

- Haz push a la rama (git push origin nueva-rama).

- Abre un Pull Request.
