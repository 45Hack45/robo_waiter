from gpiozero import DistanceSensor
from time import sleep

sensor1 = DistanceSensor(27, 22, max_distance=1, threshold_distance=0.5)
sensor2 = DistanceSensor(23, 17, max_distance=1, threshold_distance=0.5)

while True:
    print('Distance 1 to nearest object is', sensor1.distance, 'm')
    print('Distance 2 to nearest object is', sensor2.distance, 'm')
    sleep(1)