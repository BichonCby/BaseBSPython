#!/usr/bin/env python3
# -*-coding:Latin-1 -*

""" Programme de test unitaire des chaque interface
"""
import time
from ev3dev2.motor import OUTPUT_B,LargeMotor
from ev3dev2.led import Leds
from ev3dev2.display import Display
import ev3dev2.fonts as fonts
from ev3dev2.sensor import *

#test des LED
gyro1 = GyroSensor(INPUT_1)

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
#time.sleep(2)
top=time.time()

while time.time()-top < 10:
    ecrit('capteur :'+str(gyro1.value()))
    time.sleep(0.1)
