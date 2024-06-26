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

Boton_on = False


forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, frequency=1000)  
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, frequency=1000)    
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, frequency=1000)  
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, frequency=1000)

table = 0
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

def rotateRight():  
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
    
        if(table == 4):
            table = 1
        else:
            table += 1
            
        allStop()
        rotateRight()
        sleep(1) 
        allStop()
        sleep(1)
        
        start_time = time()
        move_duration = 5
        while (time() - start_time) < move_duration:
            if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                waitUntilClear()
                start_time = time()
            forwardDrive()
            sleep(0.1)
        
        allStop()
        sleep(5)
        
        if Boton_on:
            #Juntarlo con lo del audio
            queue.put(table)
        
        sleep(2)
    else:
        comanda = queue.get()
        weight = hx.get_weight_mean(10)
        if(weight > 0.1):
            while(table != comanda):
                if(table == 4):
                    table = 1
                else:
                    table += 1
                    
                allStop()
                rotateRight()
                sleep(1) 
                allStop()
                sleep(1)
                
                start_time = time()
                move_duration = 5
                while (time() - start_time) < move_duration:
                    if sensor1.distance < 0.5 or sensor2.distance < 0.5:
                        waitUntilClear()
                        start_time = time()
                    forwardDrive()
                    sleep(0.1)
                
                allStop()
                sleep(5)
            while(weight > 0.1):
                weight = hx.get_weight_mean(10)
                
            
            