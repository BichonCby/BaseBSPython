#!/usr/bin/env python3
# -*-coding:Latin-1 -*

import time
from Definitions import *
#from ev3dev2.motor import OUTPUT_B,LargeMotor
from ev3dev2.sensor import *
#from AddSensors import AngleSensor
from ev3dev2.sensor.lego import TouchSensor
import Trace


trace = Trace.Trace()
i=0
toucher = TouchSensor(INPUT_3)
trace
while i<50:
    top = time.time()
    i=i+1
    toucher.value()
    duration = (time.time()-top)
    trace.Log('%d\n' %(duration*1000))

trace.Close()
