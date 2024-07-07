import speech_to_text_robowaiter
import pyaudio
import wave
import threading
from gpiozero import Button
from signal import pause

# Configuración de PyAudio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
AUDIO_OUTPUT_FILENAME = "grabacion.wav"

# Configuración de GPIO
button = Button(17)  # Usando el pin GPIO 17

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
    diccionario = speech_to_text_robowaiter.speech_to_text()
    return diccionario  
    
def stop_recording():
    global is_recording
    is_recording = False
    
def main(start):
    if start:
        recording_thread = threading.Thread(target=start_recording)
        recording_thread.start()
        button.when_pressed = stop_recording

diccionario = button.when_pressed = main(True)
print(diccionario)

pause()
