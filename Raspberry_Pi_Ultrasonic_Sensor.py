from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(27, 22, max_distance=2, threshold_distance=1.5)
led = LED(26)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()
