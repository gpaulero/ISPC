import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1710",
        database="bdfacu"
    )

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            descripcion TEXT,
            prioridad INT,
            fecha_vencimiento DATE,
            categoria_id INT,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    """)

    conexion.commit()
    cursor.close()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()
    print("Tablas creadas exitosamente.")
