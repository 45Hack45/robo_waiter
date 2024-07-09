from gpiozero import PWMOutputDevice, DistanceSensor, Button, MCP3008
from time import pause, sleep

PWM_FORWARD_LEFT_PIN = 26
PWM_REVERSE_LEFT_PIN = 19
PWM_FORWARD_RIGHT_PIN = 13
PWM_REVERSE_RIGHT_PIN = 6
adc = MCP3008(channel=0)
sensor1 = DistanceSensor(27, 22, max_distance=1, threshold_distance=0.3)
sensor2 = DistanceSensor(23, 17, max_distance=1, threshold_distance=0.3)
boton = Button(16)
Boton_on = False

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, frequency=1000)  
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, frequency=1000)    
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, frequency=1000)  
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, frequency=1000)

def leer_valor_adc():
    valor_adc = adc.value
    voltaje = valor_adc * 5.0
    return voltaje

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

def reverseDrive():  	
    forwardLeft.value = 0 
    reverseLeft.value = 1.0  	
    forwardRight.value = 0  	
    reverseRight.value = 1.0  

boton.when_activated = cambio()

x = 0

while (x != 2):
    if (sensor1.distance < 0.3 or sensor2.distance < 0.3):
        forwardDrive()
        sleep(3)
    else:
        allStop()
        pause.until(sensor1.distance > 0.3 and sensor2.distance > 0.3) 
    sleep(5)
    if(Boton_on):
        while(Boton_on == True):
            voltaje = leer_valor_adc()
    sleep(1)
    if (sensor1.distance < 0.3 or sensor2.distance < 0.3):
        reverseDrive()
        sleep(3)
    else:
        allStop()
        pause.until(sensor1.distance > 0.3 and sensor2.distance > 0.3)
    sleep(5)
    if(Boton_on):
        while(Boton_on == True):
            voltaje = leer_valor_adc()
    sleep(1)
    x += 1
    
