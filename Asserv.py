# -*-coding:Latin-1 -*
import sys
import os

from Definitions import *

#if sys.platform != 'win32':
#from ev3dev2.motor import OUTPUT_B
from  ev3dev2.motor import OUTPUT_B

class Asserv:
    """ Classe qui va g�rer l'asservissement du robot.
    la fonction CalculAsserv va �tre appel�e de mani�re r�cursive par l'ext�rieur
    elle va faire appel � diff�rentes sous fonctions (g�n�ration trajectoire, etc..)
    la finalit� est de piloter les moteurs de propulsion (BO/BF)
    """
    def GenerateVirtualSpeed(self):
        #d�termination des consignes d'avance et de rotation

        #selon le type, on d�finit la distance et l'angle restant
        if self.Type == 'Auto':
            self.Distance = 50
        elif self.Type == 'Nul':
            self.Distance = 25
        self.Angle = 5
        # puis les consignes d'avance et de rotation
        self.SpdAvCns = 3*self.Distance #le PID
        self.SpdRotCns = 5*self.Angle #le PID
        #print('sys = ',sys.path)
        self.Converge = True
    def DriveWheels(self):
        #d�termination des consignes droite et gauche et pilotage des moteurs
        self.SpdWhlRightCns+=1
        self.SpdWhlLeftCns+=2
        #print('Tgtx=',self.TgtX)
    def DetermineBlocage(self):
        #si la vitesse est nulle alors que la consigne ne l'est pas
        #on peut faire un blocage par roue, ou en avance et rotation
        #il faut rajouter des temps des confirmation
        self.Blocage = not self.Blocage
    def CalculAsserv(self):
        #appel s�quentiel
        self.GenerateVirtualSpeed()
        self.DriveWheels()
    def __init__(self,pos,rob):
        self.Converge = False
        self.Distance = 0 #distance restant � parcourir
        self.Angle = 0
        self.SpdAvCns = 0
        self.SpdRotCns = 0
        self.SpdWhlRightCns = 0
        self.SpdWhlLeftCns=0
        self.Blocage = False
        self.TgtX = 0
        self.TgtY = 0
        self.Type = 'Nul';
        self.position = pos
        self.robot=rob
        #self.Type = MOVE_NUL

if __name__ == "__main__":
    a=Asserv()
    print('blocage vaut :',a.Blocage)
    a.DetermineBlocage()
    print('blocage vaut :',a.Blocage)
    a.DetermineBlocage()
    print('blocage vaut :',a.Blocage)
