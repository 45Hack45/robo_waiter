from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(7, 11, max_distance=1, threshold_distance=0.2)
led = LED(37)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()