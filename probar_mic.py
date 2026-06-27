import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as fuente:
    print("Ajustando al ruido ambiente...")
    recognizer.adjust_for_ambient_noise(fuente, duration=1)
    print("Habla ahora (tienes 5 segundos)...")
    audio = recognizer.listen(fuente, timeout=5, phrase_time_limit=10)
    print("Procesando...")
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Escuché: {texto}")
    except sr.UnknownValueError:
        print("No entendí lo que dijiste")
    except sr.RequestError as e:
        print(f"Error de conexión: {e}")