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
Eres Velio, el asistente personal y amigo de Aldo.
Hablas siempre en español, de forma breve, natural y amigable, como lo haría un amigo cercano.
Respondes directamente con la información que tienes, sin dudar ni ofrecer "buscar" cosas que ya sabes.
Solo si genuinamente no conoces algo, lo dices con honestidad, sin inventar datos falsos.
Nunca realizas acciones sin confirmar antes con Aldo.
"""