-- datos.sql

USE gestor_tareas;

INSERT INTO categorias (nombre) VALUES
('Trabajo'),
('Personal');

INSERT INTO tareas (nombre, descripcion, prioridad, fecha_vencimiento, categoria_id) VALUES
('Completar informe', 'Terminar el informe anual', 1, '2024-07-01', 1),
('Comprar regalos', 'Comprar regalos de cumpleaños', 2, '2024-07-05', 2);