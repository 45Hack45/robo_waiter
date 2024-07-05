from gpiozero import Robot, Motor
from gpiozero import PWMOutputDevice, DistanceSensor
from time import pause
from time import sleep

PWM_FORWARD_LEFT_PIN = 26
PWM_REVERSE_LEFT_PIN = 19
PWM_FORWARD_RIGHT_PIN = 13
PWM_REVERSE_RIGHT_PIN = 6

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, frequency=1000)  
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, frequency=1000)    
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, frequency=1000)  
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, frequency=1000)

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

forwardDrive()
sleep(30)
