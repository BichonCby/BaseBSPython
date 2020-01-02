#!/usr/bin/env python3
# -*-coding:Latin-1 -*

""" Programme principal du robot 2020
dans ce fichier on g�re les differentes t�ches (AU, Sequence, etc...)
"""
global asserv, robot, sensor, action, position

import Robot
import Position
import Asserv
import time
import Sensor
import Action
import MoveManager
from Definitions import *
from threading import Thread
from Strategy import *
from ev3dev2.motor import OUTPUT_B,LargeMotor
from ev3dev2.led import Leds

#On definit toutes les classes utiles, dans l'ordre car elles sont interdependantes

robot=Robot.Robot()
sensor=Sensor.Sensor(robot)
action = Action.Action(robot,sensor)
position=Position.Position(robot,sensor)
asserv = Asserv.Asserv(position,robot)
mov = MoveManager.MoveManager(asserv,robot)
temps = time.time()

print('mov = ',mov.id)
#D�finition du thread de gestion du temps de match, de la tirette et du BAU
class DureeMatch(Thread):
    """ Tread chargé de gérer la duree du match et le bouton d'arrêt d'urgence"""

    def __init__(self):
        Thread.__init__(self)
        self.debut=time.time()

    def run(self):
        """le code � executer"""
        print('debut du programme')
        while sensor.Tirette == True:
            time.sleep(0.1)
        # on est en match
        debut = time.time()
        print('debut du match')
        robot.MatchEnCours = True
        top = time.time()
        while top-debut < 100 and sensor.BAU == False:
            time.sleep(0.1)
            top = time.time()
        robot.MatchEnCours = False
        print('fin du match')

class Sequence(Thread):
    """ Tread charg� de lancer les fonctions r�currentes"""

    def __init__(self):
        Thread.__init__(self)
        self.cptseq = 0

    def run(self):
        """ Le code � executer quand le thread est lanc� """
        while robot.MatchEnCours == False:
            # avant la tirette
            top = time.time()
            print('.', end='')
            position.CalculPosition()
            sensor.ReadTCHMUX()
            action.ActionState()
            self.cptseq = self.cptseq+1
            if self.cptseq == 10:# une fois sur x, pour all�ger
                self.cptseq = 0
                robot.DisplayScore()
            pass # rajouter tout ce qui doit se passer avant la tirette, penser aux tests actionneurs
            time.sleep(robot.StepTime - (time.time()-top))
        # ####################################""
        # le match a commenc�
        while robot.MatchEnCours == True:
            # juste apr�s la tirette
            top = time.time()
            print('.', end='')
            #print('posx=',position.X)
            sensor.ReadEncoder()
            sensor.ReadTCHMUX()
            position.CalculPosition()
            asserv.CalculAsserv()
            pass # rajouter tout ce qui doit se passer pendant le match
            self.cptseq = self.cptseq+1
            if self.cptseq == 10:# une fois sur x, pour all�ger
                self.cptseq = 0
                robot.DisplayScore()
            # if faut faire un test pour voir si on tient les 20ms
            time.sleep(max(0,robot.StepTime - (time.time()-top)))
        # ####################################""
        # le match est termin�
        robot.DisplayScore()
        while sensor.Tirette == False:
            # on n'arr�te le programme que si on remet la tirette
            time.sleep(1);# on n'est pas � une seconde pr�s


""" maintenant on lance le vrai programme"""

sensor.ReadTCHMUX()
# cr�ation du thread
Duree = DureeMatch()
Seq = Sequence()
#lancement du thread de temps de match
Duree.start()
Seq.start()
InitRobot() # phase d'init, tests actionneurs
time.sleep(1) # test d'attente tirette pdt 1s
sensor.Tirette=False
while sensor.Tirette == True:
    time.sleep(0.02)
    #definition du thread de match et lancement
print('mov = ',mov.id)
match = MatchRobot(mov,asserv,robot,action)
#initRobot()
match.start()
print('mov = ',mov.id)



# pour les tests, on garde la suite, sinon on fera une boucle infinie
time.sleep(1)
position.SetPosition(20,30,25)
#m = LargeMotor(OUTPUT_B)
#m.on_for_rotations(SpeedPercent(75), 5)
leds = Leds()
leds.set_color("LEFT", "RED")
sensor.BAU = True
time.sleep(1)
sensor.Tirette=True
#time.sleep(10)
