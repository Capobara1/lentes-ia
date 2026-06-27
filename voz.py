import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3
import numpy as np
import tempfile
import os
from config import IDIOMA_VOZ, DURACION_SILENCIO, NOMBRE_ASISTENTE

VOZ_FIJA_ID = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0"

motor_voz = None

def hablar(texto):
    """Velio habla en voz alta."""
    print(f"{NOMBRE_ASISTENTE}: {texto}")

    motor = pyttsx3.init()
    motor.setProperty('rate', 150)
    motor.setProperty('volume', 1.0)
    motor.setProperty('voice', VOZ_FIJA_ID)
    motor.say(texto)
    motor.runAndWait()
    motor.stop()
    del motor

def escuchar():
    """Escucha el micrófono y devuelve texto."""
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.5  # Segundos de silencio antes de cortar la frase
    
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