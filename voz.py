import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3
import numpy as np
import tempfile
import os
from config import IDIOMA_VOZ, DURACION_SILENCIO, NOMBRE_ASISTENTE

# Motor de voz
motor_voz = pyttsx3.init()
motor_voz.setProperty('rate', 150)  # Velocidad de habla
motor_voz.setProperty('volume', 1.0)

# Configurar voz en español si está disponible
voces = motor_voz.getProperty('voices')
for voz in voces:
    if 'spanish' in voz.name.lower() or 'es' in voz.id.lower():
        motor_voz.setProperty('voice', voz.id)
        break

def hablar(texto):
    """Velio habla en voz alta."""
    print(f"{NOMBRE_ASISTENTE}: {texto}")
    motor_voz.say(texto)
    motor_voz.runAndWait()

def escuchar():
    """Escucha el micrófono y devuelve texto."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as fuente:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(fuente, duration=1)
        try:
            audio = recognizer.listen(fuente, timeout=5, phrase_time_limit=15)
            texto = recognizer.recognize_google(audio, language="es-ES")
            print(f"Tú: {texto}")
            return texto
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            hablar("No tengo conexión para procesar el audio.")
            return None