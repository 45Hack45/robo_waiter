from gpiozero import Robot, Motor, DistanceSensor
from time import pause

robot = Robot(left=Motor(26, 19), right=Motor(13, 6))
sensor1 = DistanceSensor(27, 22, max_distance=1, threshold_distance=0.4)

sensor1.when_in_range = robot.stop()
sensor1.when_out_of_range = robot.forward()
pause()