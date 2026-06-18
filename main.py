import sys
from config import NOMBRE_ASISTENTE, NOMBRE_USUARIO
from memoria import agregar_mensaje, guardar_conversacion, limpiar_historial
from agente import preguntar_a_velio
from voz import hablar, escuchar

def modo_texto():
    """Conversa con Velio escribiendo."""
    print(f"\n{'='*40}")
    print(f"  {NOMBRE_ASISTENTE} - Asistente Personal")
    print(f"{'='*40}")
    print("Escribe 'salir' para terminar.")
    print("Escribe 'limpiar' para borrar el historial.\n")

    hablar(f"Hola {NOMBRE_USUARIO}, soy {NOMBRE_ASISTENTE}. ¿En qué te puedo ayudar?")

    while True:
        try:
            entrada = input(f"{NOMBRE_USUARIO}: ").strip()

            if not entrada:
                continue

            if entrada.lower() == "salir":
                guardar_conversacion()
                hablar("Hasta luego, fue un placer ayudarte.")
                break

            if entrada.lower() == "limpiar":
                limpiar_historial()
                print("Historial limpiado.")
                continue

            respuesta = preguntar_a_velio(entrada)
            hablar(respuesta)

        except KeyboardInterrupt:
            guardar_conversacion()
            hablar("Hasta luego.")
            break

def modo_voz():
    """Conversa con Velio por micrófono."""
    print(f"\n{'='*40}")
    print(f"  {NOMBRE_ASISTENTE} - Modo Voz")
    print(f"{'='*40}")
    print("Habla cuando veas 'Escuchando...'")
    print("Presiona Ctrl+C para salir.\n")

    hablar(f"Hola {NOMBRE_USUARIO}, estoy escuchándote.")

    while True:
        try:
            texto = escuchar()

            if texto is None:
                continue

            if "salir" in texto.lower() or "adiós" in texto.lower():
                guardar_conversacion()
                hablar("Hasta luego, fue un placer ayudarte.")
                break

            respuesta = preguntar_a_velio(texto)
            hablar(respuesta)

        except KeyboardInterrupt:
            guardar_conversacion()
            hablar("Hasta luego.")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "voz":
        modo_voz()
    else:
        modo_texto()