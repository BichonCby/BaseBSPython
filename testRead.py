#!/usr/bin/env python3
# -*-coding:Latin-1 -*

import time
from Definitions import *
#from ev3dev2.motor import OUTPUT_B,LargeMotor
from ev3dev2.sensor import *
from AddSensors import AngleSensor
from ev3dev2.sensor.lego import TouchSensor
import Trace


trace = Trace.Trace()
i=0
toucher = TouchSensor(INPUT_3)
EncoderSensRight = AngleSensor(INPUT_1)
EncoderSensLeft = AngleSensor(INPUT_2)
trace.Log('toto\n')
while i<50:
    top = time.time()
    i=i+1
    #toucher.value()
    fic=open('/sys/class/lego-sensor/sensor0/value0','r')
    val = fic.read()
    fic.close()
    duration = (time.time()-top)
    trace.Log(val + ': %.2f\n' %(duration*1000))
    time.sleep(0.1)

trace.Close()
