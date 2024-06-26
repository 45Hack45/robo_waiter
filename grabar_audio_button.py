import pyaudio
import wave
from gpiozero import Button
from signal import pause
from threading import Thread, Timer

# Parámetros de grabación
FORMATO = pyaudio.paInt16
CANALES = 1
RATE = 44100
CHUNK = 1024
archivo_salida = "grabacion.wav"
grabando = False
hilo_grabacion = None
temporizador = None
TIEMPO_LIMITE = 50  # Tiempo límite en segundos

# Crear la instancia del botón
boton = Button(17)

# Función para grabar el audio
def grabar_audio():
    global grabando
    audio = pyaudio.PyAudio()

    # Iniciar la grabación
    stream = audio.open(format=FORMATO, channels=CANALES,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    
    print("Grabando...")

    frames = []

    while grabando:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Grabación completada.")

    # Detener la grabación
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Guardar el audio en un archivo WAV
    with wave.open(archivo_salida, 'wb') as archivo_wave:
        archivo_wave.setnchannels(CANALES)
        archivo_wave.setsampwidth(audio.get_sample_size(FORMATO))
        archivo_wave.setframerate(RATE)
        archivo_wave.writeframes(b''.join(frames))

    print(f"Archivo guardado como {archivo_salida}")

# Función para detener la grabación
def detener_grabacion():
    global grabando, hilo_grabacion, temporizador
    grabando = False
    if hilo_grabacion is not None:
        hilo_grabacion.join()
    if temporizador is not None:
        temporizador.cancel()
    print("Grabación detenida.")

# Función para alternar la grabación
def alternar_grabacion():
    global grabando, hilo_grabacion, temporizador

    if grabando:
        detener_grabacion()
    else:
        grabando = True
        hilo_grabacion = Thread(target=grabar_audio)
        hilo_grabacion.start()
        temporizador = Timer(TIEMPO_LIMITE, detener_grabacion)
        temporizador.start()
        print("Grabación iniciada.")

# Asignar la función de alternar grabación al evento de presionar el botón
boton.when_pressed = alternar_grabacion

# Mantener el programa en ejecución
pause()
