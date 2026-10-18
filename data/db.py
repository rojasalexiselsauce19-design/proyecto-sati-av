import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",            # usuario MySQL
        password="1999",        # contraseña MySQL
        database="sati_av"      # nombre de la base de datos
    )

def inicializar_bd():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS solicitudes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            carnet VARCHAR(50) NOT NULL,
            carrera VARCHAR(100) NOT NULL,
            motivo TEXT NOT NULL
        )
    """)
    conexion.commit()
    cursor.close()
    conexion.close()

def guardar_solicitud_desbloqueo(carnet, carrera, motivo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM solicitudes WHERE carnet = %s", (carnet,))
    existe = cursor.fetchone()[0]

    if existe > 0:
        cursor.close()
        conexion.close()
        return "Error: Carnet ya registrado"
    else:
        sql = "INSERT INTO solicitudes (carnet, carrera, motivo) VALUES (%s, %s, %s)"
        valores = (carnet, carrera, motivo)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return "Solicitud registrada con éxito"




      
    