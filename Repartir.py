from gpiozero import PWMOutputDevice, DistanceSensor, Button
from time import sleep, time


PWM_FORWARD_LEFT_PIN = 26
PWM_REVERSE_LEFT_PIN = 19
PWM_FORWARD_RIGHT_PIN = 13
PWM_REVERSE_RIGHT_PIN = 6


sensor1 = DistanceSensor(echo=27, trigger=22, max_distance=1, threshold_distance=0.5)
# sensor2 = DistanceSensor(echo=23, trigger=17, max_distance=1, threshold_distance=0.5)
boton = Button(16)

Boton_on = False


forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, frequency=1000)  
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, frequency=1000)    
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, frequency=1000)  
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, frequency=1000)

table = 1


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
    while sensor1.distance < 0.5:
    # while sensor1.distance < 0.5 or sensor2.distance < 0.5:
        allStop()
        sleep(0.1)

boton.when_pressed = cambio


while True:
    start_time = time()
    move_duration = 5
    while (time() - start_time) < move_duration:
        print("Run!")
        if sensor1.distance < 0.5:
            print("Wait!!")
        # if sensor1.distance < 0.5 or sensor2.distance < 0.5:
            waitUntilClear()
            start_time = time()
        forwardDrive()
        sleep(0.1)
    
    allStop()
    rotateRight()
    sleep(1) 
    allStop()
    sleep(5)
    
    if Boton_on:
        print('Esperando.')
        while Boton_on:
            print('.')
            sleep(1)  
            
    if(table == 4):
        table = 1
    else:
        table += 1