from gpiozero import PWMOutputDevice, DistanceSensor, Button
from time import sleep
from queue import Queue
from HX711 import *
import grabar_audio_button

PWM_FORWARD_LEFT_PIN = 26
PWM_REVERSE_LEFT_PIN = 19
PWM_FORWARD_RIGHT_PIN = 13
PWM_REVERSE_RIGHT_PIN = 6


sensor1 = DistanceSensor(echo=27, trigger=22, max_distance=1, threshold_distance=0.5)
sensor2 = DistanceSensor(echo=23, trigger=17, max_distance=1, threshold_distance=0.5)
boton = Button(16)
hx = SimpleHX711(2, 3, -370, -367471)
hx.setUnit(Mass.Unit.G)
hx.zero()
print(float(str(hx.weight(35))[:-2]))

Boton_on = True


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

tiempo = 15
sleep(5)
if(Boton_on == False):
    grabar_audio_button.alternar_grabacion(False)
    print('Grabando.')
    while(Boton_on == False or tiempo > 0):
        print('.')
        sleep(1)
        tiempo = tiempo - 1
    grabar_audio_button.alternar_grabacion(True)

sleep(1)

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
        
        tiempo = 15
        sleep(5)
        if(Boton_on == False):
            grabar_audio_button.alternar_grabacion(False)
            print('Grabando.')
            while(Boton_on == False or tiempo > 0):
                print('.')
                sleep(1)
                tiempo = tiempo - 1
            grabar_audio_button.alternar_grabacion(True)
        
        allStop()
        rotateBack()
        sleep(2) 
        allStop()
        sleep(1)
    else:
        comanda = queue.get()
        if(table == 2):
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
        else:
            allStop()
            rotateBack()
            sleep(2) 
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
        
            
        
        print("Esperando. Ponga el peso.")
        weight = float(str(hx.weight(35))[:-2])
        while(weight < 0.1):
            weight = float(str(hx.weight(35))[:-2])

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
            sleep(1)
        
        print("Quite el peso")
        while(weight > 0.1):
            weight = float(str(hx.weight(35))[:-2])
        
        if(comanda == 2):
            allStop()
            rotateBack()
            sleep(2) 
            allStop()
            sleep(1)