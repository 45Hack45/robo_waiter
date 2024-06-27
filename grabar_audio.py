import pyaudio
import wave

def grabar_audio(duracion, archivo_salida):
    # Parámetros de grabación
    formato = pyaudio.paInt16  # Formato de audio
    canales = 1                # Número de canales
    tasa_muestreo = 44100      # Tasa de muestreo
    tamano_bloque = 1024       # Tamaño del bloque de datos

    audio = pyaudio.PyAudio()

    # Iniciar la grabación
    stream = audio.open(format=formato, channels=canales,
                        rate=tasa_muestreo, input=True,
                        frames_per_buffer=tamano_bloque)

    print("Grabando...")

    frames = []

    # Grabar el audio
    for _ in range(0, int(tasa_muestreo / tamano_bloque * duracion)):
        data = stream.read(tamano_bloque)
        frames.append(data)

    print("Grabación completada.")

    # Detener la grabación
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Guardar el audio en un archivo WAV
    with wave.open(archivo_salida, 'wb') as archivo_wave:
        archivo_wave.setnchannels(canales)
        archivo_wave.setsampwidth(audio.get_sample_size(formato))
        archivo_wave.setframerate(tasa_muestreo)
        archivo_wave.writeframes(b''.join(frames))

    print(f"Archivo guardado como {archivo_salida}")

# Parámetros de grabación
duracion_segundos = 10  # Duración de la grabación en segundos
nombre_archivo_salida = "grabacion.wav"  # Nombre del archivo de salida

# Llamar a la función para grabar el audio
grabar_audio(duracion_segundos, nombre_archivo_salida)