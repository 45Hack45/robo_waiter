
from gpiozero import PWMOutputDevice, DistanceSensor, Button
from time import sleep
from queue import Queue
from HX711 import *
import speech_to_text_robowaiter
import grabar_audio_button

boton = Button(16)
Boton_on = False


def cambio():
    global Boton_on
    Boton_on = not Boton_on

boton.when_pressed = cambio

if Boton_on:
    print('Esperando.')
    grabar_audio_button.main(Boton_on)
    diccionario = speech_to_text_robowaiter.speech_to_text()
    print(diccionario)

sleep(2)
