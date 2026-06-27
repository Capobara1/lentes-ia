import os
from config import PERMISO_ARCHIVOS

CARPETA_TRABAJO = "archivos_velio"

# Crear carpeta de trabajo si no existe
if not os.path.exists(CARPETA_TRABAJO):
    os.makedirs(CARPETA_TRABAJO)

def crear_archivo(nombre_archivo, contenido):
    """Crea un archivo nuevo con el contenido dado."""
    if not PERMISO_ARCHIVOS:
        return "No tengo permiso para crear archivos. Activa PERMISO_ARCHIVOS en config.py."

    try:
        ruta = os.path.join(CARPETA_TRABAJO, nombre_archivo)
        if os.path.exists(ruta):
            return f"El archivo '{nombre_archivo}' ya existe. Usa modificar si quieres cambiarlo."
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        return f"Archivo '{nombre_archivo}' creado correctamente en {CARPETA_TRABAJO}."
    except Exception as e:
        return f"No pude crear el archivo: {str(e)}"

def leer_archivo(nombre_archivo):
    """Lee el contenido de un archivo existente."""
    if not PERMISO_ARCHIVOS:
        return "No tengo permiso para leer archivos."

    try:
        ruta = os.path.join(CARPETA_TRABAJO, nombre_archivo)
        if not os.path.exists(ruta):
            return f"No encontré el archivo '{nombre_archivo}'."
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        return contenido
    except Exception as e:
        return f"No pude leer el archivo: {str(e)}"

def modificar_archivo(nombre_archivo, nuevo_contenido):
    """Sobrescribe un archivo existente con nuevo contenido."""
    if not PERMISO_ARCHIVOS:
        return "No tengo permiso para modificar archivos."

    try:
        ruta = os.path.join(CARPETA_TRABAJO, nombre_archivo)
        if not os.path.exists(ruta):
            return f"No encontré el archivo '{nombre_archivo}' para modificar."
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)
        return f"Archivo '{nombre_archivo}' modificado correctamente."
    except Exception as e:
        return f"No pude modificar el archivo: {str(e)}"

def listar_archivos():
    """Lista todos los archivos en la carpeta de trabajo."""
    if not PERMISO_ARCHIVOS:
        return "No tengo permiso para acceder a archivos."

    try:
        archivos = os.listdir(CARPETA_TRABAJO)
        if not archivos:
            return "No hay archivos todavía."
        return "Archivos disponibles: " + ", ".join(archivos)
    except Exception as e:
        return f"No pude listar archivos: {str(e)}"

def eliminar_archivo(nombre_archivo):
    """Elimina un archivo, SIEMPRE requiere confirmación previa del usuario en main.py."""
    if not PERMISO_ARCHIVOS:
        return "No tengo permiso para eliminar archivos."

    try:
        ruta = os.path.join(CARPETA_TRABAJO, nombre_archivo)
        if not os.path.exists(ruta):
            return f"No encontré el archivo '{nombre_archivo}'."
        os.remove(ruta)
        return f"Archivo '{nombre_archivo}' eliminado."
    except Exception as e:
        return f"No pude eliminar el archivo: {str(e)}"