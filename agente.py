import requests
import json
from config import MODELO_LLM, OLLAMA_URL, PERSONALIDAD, NOMBRE_USUARIO
from memoria import agregar_mensaje, obtener_historial

def preguntar_a_velio(mensaje_usuario):
    """Envía un mensaje a Velio y obtiene respuesta."""
    
    # Agregar mensaje del usuario al historial
    agregar_mensaje("user", mensaje_usuario)
    
    # Construir mensajes con personalidad + historial
    mensajes = [
        {"role": "system", "content": PERSONALIDAD}
    ] + obtener_historial()
    
    try:
        respuesta = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": MODELO_LLM,
                "messages": mensajes,
                "stream": False
            },
            timeout=30
        )
        
        if respuesta.status_code == 200:
            contenido = respuesta.json()["message"]["content"]
            agregar_mensaje("assistant", contenido)
            return contenido
        else:
            return "Tuve un problema al procesar tu mensaje."
            
    except requests.exceptions.ConnectionError:
        return "No puedo conectarme al modelo. Verifica que Ollama esté corriendo."
    except requests.exceptions.Timeout:
        return "El modelo tardó demasiado en responder, intenta de nuevo."
    except Exception as e:
        return f"Ocurrió un error inesperado: {str(e)}"

def buscar_en_web(query):
    """Búsqueda básica en DuckDuckGo."""
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            resultados = list(ddgs.text(query, max_results=3))
            if resultados:
                resumen = "\n".join([r['body'] for r in resultados])
                return resumen
            return "No encontré resultados."
    except ImportError:
        return "Módulo de búsqueda no instalado."
    except Exception as e:
        return f"Error en búsqueda: {str(e)}"