from gpiozero import PWMOutputDevice, DistanceSensor, Button
from time import sleep
from queue import Queue
from HX711 import *

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
    print('Esperando.')
    while(Boton_on == True):
        print('.')
        sleep(0.5)
        
    queue.put(table)
    print('Has pedido una hamburguesa')

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
            print('Esperando.')
            while(Boton_on == True):
                print('.')
                sleep(0.5)
                
            queue.put(table)
            print('Has pedido una hamburguesa')

        sleep(2)

        if(queue.empty()):
            allStop()
            rotateBack()
            sleep(2.2) 
            allStop()
            sleep(1)
    else:
        comanda = queue.get()
        if(table == 2):
            
            allStop()
            rotateBack()
            sleep(2.2) 
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
        sleep(2.2) 
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
            sleep(2.2) 
            allStop()
            sleep(1)
