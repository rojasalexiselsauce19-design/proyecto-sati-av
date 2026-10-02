import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data.db import obtener_conexion


def guardar_solicitud_desbloqueo(carnet, carrera, motivo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = "INSERT INTO solicitudes (carnet, carrera, motivo, estado) VALUES (%s, %s, %s, 'Pendiente')"
    cursor.execute(query, (carnet, carrera, motivo))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_solicitudes(carnet):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = "SELECT id, carnet, carrera, motivo, estado FROM solicitudes WHERE carnet = %s"
    cursor.execute(query, (carnet,))
    solicitudes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return solicitudes

def cambiar_estado_desbloqueo(id_solicitud, nuevo_estado="Aprobado"):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = "UPDATE solicitudes SET estado = %s WHERE id = %s"
    cursor.execute(query, (nuevo_estado, id_solicitud))
    conexion.commit()
    cursor.close()
    conexion.close()

if __name__ == "__main__":
    guardar_solicitud_desbloqueo("1234", "Ingeniería en Sistemas", "Necesito desbloquear acceso")
    solicitudes = obtener_solicitudes("1234")
    print("Solicitudes obtenidas:", solicitudes)

    if solicitudes:
        primera_id = solicitudes[0][0]
        cambiar_estado_desbloqueo(primera_id, "Aprobado")
        print(f"Solicitud con id {primera_id} cambiada a 'Aprobado'.")
        solicitudes_actualizadas = obtener_solicitudes("1234")
        print("Solicitudes actualizadas:", solicitudes_actualizadas)
