import vosk
import sounddevice as sd
import queue
import json

RUTA_MODELO = "vosk-model-small-es-0.42"
PALABRA_ACTIVACION = "velio"

modelo = vosk.Model(RUTA_MODELO)
cola_audio = queue.Queue()

def callback_audio(indata, frames, time, status):
    cola_audio.put(bytes(indata))

def esperar_wake_word():
    """Escucha continuamente hasta detectar la palabra de activación."""
    reconocedor = vosk.KaldiRecognizer(modelo, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                            channels=1, callback=callback_audio):
        print(f"Esperando que digas '{PALABRA_ACTIVACION}'...")
        while True:
            data = cola_audio.get()
            if reconocedor.AcceptWaveform(data):
                resultado = json.loads(reconocedor.Result())
                texto = resultado.get("text", "")
                if PALABRA_ACTIVACION in texto.lower():
                    print(f"¡Activado! Escuché: '{texto}'")
                    return True