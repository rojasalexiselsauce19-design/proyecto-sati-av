import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data.repositorio import guardar_solicitud_desbloqueo, obtener_solicitudes
def procesar_nueva_solicitud(carnet, carrera, motivo):
    ""
    if not carnet or not carrera or not motivo:
        return False, "Error: Todos los campos son obligatorios."
        guardar_solicitud_desbloqueo(carnet, carrera, motivo)
    return True, "Solicitud procesada correctamente."

def listar_solicitudes_por_carnet(carnet):
    if not carnet:
        return []
    return obtener_solicitudes(carnet)
def cambiar_estado_solicitud(id_solicitud, nuevo_estado="Aprobado"):
    if not id_solicitud:
        return False, "Error: ID de solicitud no proporcionado."
        cambiar_estado_desbloqueo(id_solicitud, nuevo_estado)
    return True, f"Solicitud con id {id_solicitud} cambiada a '{nuevo_estado}'."