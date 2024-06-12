CREATE DATABASE bdfacu;
USE bdfacu;
CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    prioridad INT,
    fecha_vencimiento DATE,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);
