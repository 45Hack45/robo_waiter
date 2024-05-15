from gpiozero import Robot, Motor, DistanceSensor, Button, MCP3008
from time import pause, sleep

adc = MCP3008(channel=0)
robot = Robot(left=Motor(26, 19), right=Motor(13, 6))
sensor1 = DistanceSensor(27, 22, max_distance=1, threshold_distance=0.3)
sensor2 = DistanceSensor(23, 17, max_distance=1, threshold_distance=0.3)
boton = Button(16)
Boton_on = False

def leer_valor_adc():
    valor_adc = adc.value
    voltaje = valor_adc * 5.0
    return voltaje

def cambio():
    global Boton_on
    Boton_on = not Boton_on


boton.when_activated = cambio()

x = 0

while (x != 2):
    if (sensor1.distance < 0.3 or sensor2.distance < 0.3):
        robot.forward()
        sleep(3)
    else:
        robot.stop()
        pause.until(sensor1.distance > 0.3 and sensor2.distance > 0.3) 
    sleep(5)
    if(Boton_on):
        while(Boton_on == True):
            voltaje = leer_valor_adc()
    sleep(1)
    if (sensor1.distance < 0.3 or sensor2.distance < 0.3):
        robot.backward()
        sleep(3)
    else:
        robot.stop()
        pause.until(sensor1.distance > 0.3 and sensor2.distance > 0.3)
    sleep(5)
    if(Boton_on):
        while(Boton_on == True):
            voltaje = leer_valor_adc()
    sleep(1)
    x += 1
    
