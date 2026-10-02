import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",            
        password="1999", 
        database="sati_av"
    )

      
    