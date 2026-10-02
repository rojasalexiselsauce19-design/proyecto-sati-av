import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",            # tu usuario
        password="1999", # tu contraseña
        database="sati_av"
    )
    print("Conexión exitosa:", conexion.is_connected())
    conexion.close()
except Exception as e:
    print("Error:", e)
