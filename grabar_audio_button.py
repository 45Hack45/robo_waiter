import speech_to_text_robowaiter
import pyaudio
import wave
import threading
from gpiozero import Button

# Configuración de PyAudio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
AUDIO_OUTPUT_FILENAME = "output.wav"

# Configuración de GPIO
button = Button(16)  # Usando el pin GPIO 17

# Variable global para controlar la grabación
is_recording = False

def toggle_state():
    global is_recording
    is_recording = not is_recording

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
    print("Grabación guardada")
    
def stop_recording():
    global is_recording
    is_recording = False

def main():
        global is_recording

        toggle_state()

        if is_recording:
            recording_thread = threading.Thread(target=start_recording)
            recording_thread.start()

button.when_pressed = main
diccionario = speech_to_text_robowaiter.speech_to_text()
print(diccionario)
