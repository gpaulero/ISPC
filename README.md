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

**Análisis del Proyecto: Gestor de Tareas Personales**

**Objetivos del Proyecto**

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

1- main.py: Archivo principal de la aplicación. Contiene el menú de opciones y hace uso de funciones definidas en otros módulos.

2- tareas.py: Contiene las funciones relacionadas con la gestión de tareas (crear, ver, editar, eliminar). En esta etapa, las funciones solo imprimen mensajes.

3- usuarios.py: Contiene las funciones relacionadas con la gestión de usuarios. En esta etapa, las funciones solo imprimen mensajes.

4- menu.py: Contiene la lógica para mostrar el menú y manejar la navegación del usuario. Llama a las funciones definidas en tareas.py y usuarios.py.


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
