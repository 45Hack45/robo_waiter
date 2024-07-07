import pyaudio
import wave
import threading
from gpiozero import Button
import time

# Configuración de PyAudio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
AUDIO_OUTPUT_FILENAME = "grabacion.wav"

# Configuración de GPIO
stop_button = Button(16)  # Usando el pin GPIO 17 para detener la grabación

# Variable global para controlar la grabación
is_recording = False

def start_recording():
    global is_recording
    is_recording = True

    # Crear una instancia de PyAudio
    audio = pyaudio.PyAudio()

    # Abrir el flujo de audio
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    while is_recording:
        data = stream.read(CHUNK)
        frames.append(data)

    # Detener y cerrar el flujo de audio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Guardar la grabación en un archivo WAV
    wf = wave.open(AUDIO_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def stop_recording():
    global is_recording
    is_recording = False

def main(start):
    if start:
        print("Starting recording...")
        recording_thread = threading.Thread(target=start_recording)
        recording_thread.start()
        stop_button.when_pressed = stop_recording

    # Mantener el programa en ejecución
    print("Press the stop button to end recording.")
    while True:
        time.sleep(1)  # Mantener el programa en ejecución
