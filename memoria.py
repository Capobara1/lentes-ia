import json
import os
from datetime import datetime
from config import CARPETA_MEMORIA, MAX_HISTORIAL

# Crear carpeta de memoria si no existe
if not os.path.exists(CARPETA_MEMORIA):
    os.makedirs(CARPETA_MEMORIA)

historial = []

def agregar_mensaje(rol, contenido):
    """Agrega un mensaje al historial de la conversación actual."""
    historial.append({
        "role": rol,
        "content": contenido,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    # Mantener solo los últimos N mensajes
    if len(historial) > MAX_HISTORIAL:
        historial.pop(0)

def obtener_historial():
    """Devuelve el historial para enviarlo al modelo."""
    return [{"role": m["role"], "content": m["content"]} for m in historial]

def guardar_conversacion():
    """Guarda la conversación actual en un archivo."""
    if not historial:
        return
    nombre_archivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".json"
    ruta = os.path.join(CARPETA_MEMORIA, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)
    print(f"Conversación guardada en {ruta}")

def limpiar_historial():
    """Limpia el historial de la sesión actual."""
    historial.clear()