from gpiozero import DistanceSensor
from signal import pause

sensor1 = DistanceSensor(27, 22, max_distance=2, threshold_distance=1.5)
# sensor2 = DistanceSensor(23, 17, max_distance=2, threshold_distance=1.5)

def foo():
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

def boo():
    print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

sensor1.when_in_range = foo
sensor1.when_out_of_range = boo

pause()
