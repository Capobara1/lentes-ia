# Configuración general del asistente

NOMBRE_ASISTENTE = "Velio"  # Puedes cambiar el nombre aquí
NOMBRE_USUARIO = "Aldo"  # Pon tu nombre aquí

# Modelo de lenguaje
MODELO_LLM = "llama3.1:8b"
OLLAMA_URL = "http://localhost:11434"

# Configuración de voz
IDIOMA_VOZ = "es"
DURACION_SILENCIO = 2  # Segundos de silencio para detectar fin de frase

# Memoria
CARPETA_MEMORIA = "memoria_conversaciones"
MAX_HISTORIAL = 10  # Cuántos mensajes recuerda en la conversación actual

# Permisos (True = activado, False = desactivado)
PERMISO_CAMARA = False
PERMISO_ARCHIVOS = False
PERMISO_WEB = False
PERMISO_HOGAR = False

# Personalidad del asistente
PERSONALIDAD = """
Eres Velio, un asistente personal y amigo del usuario.
Tu objetivo es apoyarlo en su día a día de forma natural y conversacional.
Respondes siempre en español, de forma clara y amigable.
Cuando no sabes algo, lo dices honestamente.
Nunca ejecutas acciones sin confirmar primero con el usuario.
"""