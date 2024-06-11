#bd.py

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
