-- consultas.sql

USE gestor_tareas;

-- Consulta 1: Mostrar todas las tareas
SELECT * FROM tareas;

-- Consulta 2: Mostrar algunas columnas de tareas
SELECT nombre, prioridad, fecha_vencimiento FROM tareas;

-- Consulta 3: Mostrar tareas con prioridad alta
SELECT * FROM tareas WHERE prioridad = 1;

-- Consulta 4: Mostrar tareas con fechas de vencimiento entre dos fechas
SELECT * FROM tareas WHERE fecha_vencimiento BETWEEN '2024-07-01' AND '2024-07-10';

-- Consulta 5: Mostrar tareas limitadas a las 2 primeras
SELECT * FROM tareas LIMIT 2;

-- Consulta 6: Mostrar tareas con su categoría usando INNER JOIN
SELECT tareas.nombre, tareas.descripcion, categorias.nombre AS categoria
FROM tareas
INNER JOIN categorias ON tareas.categoria_id = categorias.id;

-- Consulta 7: Mostrar tareas con su categoría y con prioridad alta
SELECT tareas.nombre, tareas.descripcion, categorias.nombre AS categoria
FROM tareas
INNER JOIN categorias ON tareas.categoria_id = categorias.id
WHERE tareas.prioridad = 1;
