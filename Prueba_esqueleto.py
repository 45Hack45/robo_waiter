from gpiozero import PWMOutputDevice, DistanceSensor, Button
from time import sleep, time
from queue import Queue
from HX711 import *


PWM_FORWARD_LEFT_PIN = 26
PWM_REVERSE_LEFT_PIN = 19
PWM_FORWARD_RIGHT_PIN = 13
PWM_REVERSE_RIGHT_PIN = 6


sensor1 = DistanceSensor(echo=27, trigger=22, max_distance=1, threshold_distance=0.5)
sensor2 = DistanceSensor(echo=23, trigger=17, max_distance=1, threshold_distance=0.5)
boton = Button(16)
hx = SimpleHX711(20, 21, -370, -367471)
hx.setUnit(Mass.Unit.G)
hx.zero()

Boton_on = False


forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, frequency=1000)  
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, frequency=1000)    
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, frequency=1000)  
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, frequency=1000)

table = 1
queue = Queue()


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


while True:
    
    if(queue.empty()):
    
        if(table == 2):
            table = 1
        else:
            table = 2
            
        allStop()
        rotateBack()
        sleep(2) 
        allStop()
        sleep(1)
        
        tiempo = 4
        while tiempo > 0:
            if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                waitUntilClear()
            forwardDrive()
            sleep(0.1)
            tiempo = tiempo - 0.1
        
        allStop()
        sleep(5)
        
        if Boton_on:
            #Juntarlo con lo del audio
            queue.put(table)
            print('Has pedido una hamburguesa')
            cambio()
        
        sleep(2)
    else:
        comanda = queue.get()
        sleep(10)
        weight = hx.weight(35)
        if(weight > 0.1):
            while(table != comanda):
                if(table == 2):
                    table = 1
                else:
                    table = 2
                    
                allStop()
                rotateBack()
                sleep(2) 
                allStop()
                sleep(1)
                
                tiempo = 4
                while tiempo > 0:
                    if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                        waitUntilClear()
                    forwardDrive()
                    sleep(0.1)
                    tiempo = tiempo - 0.1
                
                allStop()
                sleep(5)
            while(weight > 0.1):
                weight = hx.weight(35)
                