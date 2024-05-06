#https://github.com/endail/hx711-rpi-py
from HX711 import *

hx = SimpleHX711(2, 3, -370, -367471)
hx.setUnit(Mass.Unit.G)
hx.zero()
while True:
  print(hx.weight(35))
