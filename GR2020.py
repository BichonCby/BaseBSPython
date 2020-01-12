#!/usr/bin/env python3
# -*-coding:Latin-1 -*

""" Programme principal du robot 2020
dans ce fichier on gère les differentes tâches (AU, Sequence, etc...)
"""
# global asserv, robot, sensor, action, position

import Robot

import Position
import Asserv
import time
import SensorMgt
import Action
import MoveManager
from Definitions import *
from threading import Thread
from Strategy import *
from ev3dev2.motor import OUTPUT_B,LargeMotor
from ev3dev2.led import Leds
from ev3dev2 import get_current_platform
import Trace
if get_current_platform() != 'fake':
    import os
    os.system('setfont Lat15-TerminusBold14')

#On definit toutes les classes utiles, dans l'ordre car elles sont interdependantes
print('toto')
platform = get_current_platform()
print(get_current_platform())
robot=Robot.Robot()
sensorMgt=SensorMgt.SensorMgt(robot)
action = Action.Action(robot,sensorMgt)
position=Position.Position(robot,sensorMgt)
asserv = Asserv.Asserv(position,robot)
mov = MoveManager.MoveManager(asserv,robot)
trace = Trace.Trace()

temps = time.time()

#print('mov = ',mov.id)
#D�finition du thread de gestion du temps de match, de la tirette et du BAU
class DureeMatch(Thread):
    """ Tread chargé de gérer la duree du match et le bouton d'arrêt d'urgence"""

    def __init__(self):
        Thread.__init__(self)
        self.debut=time.time()

    def run(self):
        """le code à executer"""
        print('debut du programme', str(int(time.time()-self.debut)))
        while sensorMgt.Tirette == True:
            time.sleep(0.1)
        # on est en match
        debut = time.time()
        print('debut du match', str(int(time.time()-self.debut)))
        robot.MatchEnCours = True
        top = time.time()
        while top-debut < 10 and sensorMgt.BAU == False:
            time.sleep(0.1)
            top = time.time()
        robot.MatchEnCours = False
        print('fin du match',  str(int(time.time()-self.debut)))

class Sequence(Thread):
    """ Tread chargé de lancer les fonctions récurrentes"""

    def __init__(self):
        Thread.__init__(self)
        self.cptseq = 0

    def run(self):
        """ Le code à executer quand le thread est lancé """
        print('Avant la tirette')
        while robot.MatchEnCours == False:
            # avant la tirette
            top = time.time()
            #print('.', end='')
            position.CalculPosition()
            sensorMgt.ReadTCHMUX()
            action.ActionState()
            robot.DisplayPos(position.X,position.Y,0)
            self.cptseq = self.cptseq+1
            if self.cptseq == 10:# une fois sur x, pour all�ger
                self.cptseq = 0
                robot.DisplayScore()
            pass # rajouter tout ce qui doit se passer avant la tirette, penser aux tests actionneurs
            time.sleep(max(0,robot.StepTime - (time.time()-top)))
        # ####################################""
        # le match a commencé
        print ('La tirette est tirée')
        while robot.MatchEnCours == True:
            # juste apr�s la tirette
            top = time.time()
            #print(',', end='')
            #print('posx=',position.X)
            sensorMgt.ReadEncoder()
            sensorMgt.ReadTCHMUX()
            position.CalculPosition()
            robot.DisplayPos(position.X,position.Y,position.angle)
            asserv.CalculAsserv()
            pass # rajouter tout ce qui doit se passer pendant le match
            self.cptseq = self.cptseq+1
            if self.cptseq == 10:# une fois sur x, pour alléger
                self.cptseq = 0
                #robot.DisplayScore()
            # if faut faire un test pour voir si on tient les 20ms
            time.sleep(max(0,robot.StepTime - (time.time()-top)))
        # ####################################""
        # le match est termin�
        print('La match est fini')
        robot.DisplayScore()
        while sensorMgt.Tirette == False:
            # on n'arr�te le programme que si on remet la tirette
            time.sleep(1);# on n'est pas à une seconde près


""" maintenant on lance le vrai programme"""

sensorMgt.ReadTCHMUX()
# création du thread
Duree = DureeMatch()
Seq = Sequence()
#lancement du thread de temps de match
trace.Log('voilà')
trace.Close()
Duree.start()
Seq.start()
InitRobot() # phase d'init, tests actionneurs
time.sleep(1) # test d'attente tirette pdt 1s
#sensorMgt.Tirette=False
#while sensorMgt.Tirette == True:
#    time.sleep(0.02)
    #definition du thread de match et lancement
print('mov1 = ',mov.id)
match = MatchRobot(mov,asserv,robot,action)
#initRobot()
match.start()
print('mov2 = ',mov.id)



# pour les tests, on garde la suite, sinon on fera une boucle infinie
if platform == 'fake': # on est sur PC
    print('programme PC')
    sensorMgt.Tirette=True
    time.sleep(2)
    sensorMgt.Tirette=False # on retire la tirette
    time.sleep(2)
    sensorMgt.Tirette=True # pour arreter le programme
else:
    time.sleep(20)
#position.SetPosition(20,30,25)
#mov.GoFor(400,400,0.02,5)
#mov.GoFor(400,500,0.02,5)
#mov.Rotate(90)
#mov.MoveManu(50,100)
#time.sleep(10)
#mov.MoveManu(200,100)
#time.sleep(20)
#mov.DontMove(1)
#m = LargeMotor(OUTPUT_B)
#m.on_for_rotations(SpeedPercent(75), 5)
#leds = Leds()
#leds.set_color("LEFT", "RED")
#sensorMgt.BAU = True
#time.sleep(1)
#sensorMgt.Tirette=True
#time.sleep(10)
