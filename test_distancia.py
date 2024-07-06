from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(27, 22, max_distance=1, threshold_distance=0.5)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)