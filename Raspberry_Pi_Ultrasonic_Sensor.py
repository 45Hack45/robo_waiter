from gpiozero import DistanceSensor, LED
from signal import pause

sensor1 = DistanceSensor(27, 22, max_distance=2, threshold_distance=1.5)
sensor2 = DistanceSensor(23, 17, max_distance=2, threshold_distance=1.5)
led = LED(26)

sensor2.when_in_range = led.on
sensor2.when_out_of_range = led.off

sensor1.when_in_range = led.on
sensor1.when_out_of_range = led.off

pause()
