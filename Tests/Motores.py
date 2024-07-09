from gpiozero import Robot, Motor
from time import sleep

robot = Robot(left=Motor(26, 19), right=Motor(13, 6))

robot.forward()
sleep(10)
robot.forward()
sleep(10)