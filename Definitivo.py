import pyaudio
import wave
from gpiozero import PWMOutputDevice, DistanceSensor, Button
from time import sleep
from queue import Queue
from HX711 import *
import speech_to_text_robowaiter

PWM_FORWARD_LEFT_PIN = 26
PWM_REVERSE_LEFT_PIN = 19
PWM_FORWARD_RIGHT_PIN = 13
PWM_REVERSE_RIGHT_PIN = 6

print('Antes de peso')
sensor1 = DistanceSensor(echo=27, trigger=22, max_distance=1, threshold_distance=0.5)
sensor2 = DistanceSensor(echo=23, trigger=17, max_distance=1, threshold_distance=0.5)
boton = Button(16)
hx = SimpleHX711(2, 3, -370, -367471)
hx.setUnit(Mass.Unit.G)
hx.zero()
print(float(str(hx.weight(35))[:-2]))
print('Después de peso')

Boton_on = False


forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, frequency=1000)  
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, frequency=1000)    
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, frequency=1000)  
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, frequency=1000)

table = 1
queue = Queue()

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

def cambio():
    global Boton_on
    Boton_on = not Boton_on
    
def allStop():  	
    forwardLeft.value = 0  	
    reverseLeft.value = 0  	
    forwardRight.value = 0  	
    reverseRight.value = 0 
    
def forwardDrive():  	
    forwardLeft.value = 1.0  	
    reverseLeft.value = 0  	
    forwardRight.value = 1.0 
    reverseRight.value = 0 

def rotateBack():  
    forwardLeft.value = 1.0  
    reverseLeft.value = 0  
    forwardRight.value = 0  
    reverseRight.value = 1.0

def waitUntilClear():
    while sensor1.distance < 0.5 or sensor2.distance < 0.5:
        allStop()
        sleep(0.1)

boton.when_pressed = cambio

print("Mover a mesa")
tiempo = 4
while tiempo > 0:
    if sensor1.distance < 0.5 or sensor2.distance < 0.5:
        print("Obstaculo")
        waitUntilClear()
        print("Libre")
    forwardDrive()
    sleep(0.1)
    tiempo = tiempo - 0.1

allStop()
sleep(1)

sleep(5)

if Boton_on:
    audio = pyaudio.PyAudio()

    # Iniciar la grabación
    stream = audio.open(format=FORMATO, channels=CANALES,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    
    print("Grabando...")

    frames = []

    while(Boton_on == True):
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
        diccionario = speech_to_text_robowaiter.speech_to_text()
    
        
    queue.put(table)
    print(diccionario)

sleep(2)

while True:
    
    if(queue.empty()):
        print("Mover a mesa")
        
        tiempo = 4
        while tiempo > 0:
            if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                print("Obstaculo")
                waitUntilClear()
                print("Libre")
            forwardDrive()
            sleep(0.1)
            tiempo = tiempo - 0.1
        
        allStop()
        sleep(1)
        
        if(table == 2):
            table = 1
        else:
            table = 2

        sleep(5)
        
        if Boton_on:
            archivo_salida = "grabacion.wav"
            audio = pyaudio.PyAudio()

            # Iniciar la grabación
            stream = audio.open(format=FORMATO, channels=CANALES,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    
            print("Grabando...")

            frames = []

            while(Boton_on == True):
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
                diccionario = speech_to_text_robowaiter.speech_to_text()
            
                
            queue.put(table)
            print(diccionario)
        
        sleep(2)

        if(queue.empty()):
            allStop()
            rotateBack()
            sleep(2.3) 
            allStop()
            sleep(1)
    else:
        comanda = queue.get()
        if(table == 2):
            
            allStop()
            rotateBack()
            sleep(2.3) 
            allStop()
            sleep(1)
            
            tiempo = 4
            while tiempo > 0:
                if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                    print("Obstaculo")
                    waitUntilClear()
                    print("Libre")
                forwardDrive()
                sleep(0.1)
                tiempo = tiempo - 0.1
            allStop()
            sleep(1)
            
        tiempo = 4
        while tiempo > 0:
            if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                print("Obstaculo")
                waitUntilClear()
                print("Libre")
            forwardDrive()
            sleep(0.1)
            tiempo = tiempo - 0.1
        allStop()
        sleep(1)

        allStop()
        rotateBack()
        sleep(2.3) 
        allStop()
        sleep(3)    
        
        print("Esperando. Ponga el peso.")
        weight = float(str(hx.weight(35))[:-2])
        print(float(str(hx.weight(35))[:-2]))
        while(weight < 10  or weight > 1000):
            weight = float(str(hx.weight(35))[:-2])
            print(float(str(hx.weight(35))[:-2]))
            sleep(1)

        tiempo = 4
        while tiempo > 0:
            if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                print("Obstaculo")
                waitUntilClear()
                print("Libre")
            forwardDrive()
            sleep(0.1)
            tiempo = tiempo - 0.1
        allStop()
        sleep(1)
        
        table = 1
        
        if(comanda == 2):
            table = 2
            
            tiempo = 4
            while tiempo > 0:
                if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                    print("Obstaculo")
                    waitUntilClear()
                    print("Libre")
                forwardDrive()
                sleep(0.1)
                tiempo = tiempo - 0.1
            allStop()
            sleep(3)
        
        print("Quite el peso")
        while(weight > 10):
            weight = float(str(hx.weight(35))[:-2])
            print(float(str(hx.weight(35))[:-2]))
            sleep(1)
        
        if(comanda == 2):
            allStop()
            rotateBack()
            sleep(2.3) 
            allStop()
            sleep(1)


