#!/usr/bin/env python3
# -*-coding:Latin-1 -*

""" Programme de test unitaire des chaque interface
"""
import time
from ev3dev2.motor import OUTPUT_B,LargeMotor
from ev3dev2.led import Leds
from ev3dev2.display import Display
import ev3dev2.fonts as fonts
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from AddSensors import AngleSensor
from ev3dev2.sensor import *
from ev3dev2.port import LegoPort
from math import asin, pi

#from ev3dev2.sensor import Sensor
#in1 = LegoPort(INPUT_1)
#in1.mode = 'auto'
#time.sleep(2)

#mtrmux = Sensor(INPUT_1)

#test des LED
try:
    gyro1 = GyroSensor(INPUT_1)
except:
    pass

ang = AngleSensor(INPUT_2)
#t=ang.pollms()
display = Display()
myfont = fonts.load('charBI24')
def ecrit(text):
    display.text_grid(text,x=2,y=3,font=myfont)
    display.update()

leds = Leds()
leds.set_color("LEFT", "RED")
time.sleep(2)
leds.set_color("LEFT","GREEN")
ecrit("toto")
time.sleep(2)
ecrit("tata")
#test des moteurs

m=LargeMotor(OUTPUT_B)
m.speed_sp=500
m.run_forever()
time.sleep(2)
top=time.time()

while time.time()-top < 6:
    ecrit('capteur :'+str(ang.value()))
    time.sleep(0.1)

