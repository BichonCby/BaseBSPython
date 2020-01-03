# -*-coding:Latin-1 -*
import sys
import os

from Definitions import *
from math import sqrt, asin
#from Definitions import AngleNorm
#if sys.platform != 'win32':
#from ev3dev2.motor import OUTPUT_B
from  ev3dev2.motor import OUTPUT_B

class Asserv:
    """ Classe qui va g�rer l'asservissement du robot.
    la fonction CalculAsserv va �tre appel�e de mani�re r�cursive par l'ext�rieur
    elle va faire appel � diff�rentes sous fonctions (g�n�ration trajectoire, etc..)
    la finalit� est de piloter les moteurs de propulsion (BO/BF)
    """
    """ Les types de déplacement autorisés :
    Nul : pas de déplacement, on ne pilote plus les moteurs
    Polar : asservissement automatique, qui va à un point x, y en marche avant (si distance assez grande)
    PolarRev : asservissement automatique, qui va à un point x, y en marche arrière (si distance assez grande)
    Rotation : asservissement en rotation, on ne gère que l'angle, le robot tourne autour de son centre
    Manual : pas d'asservissement, on pilote les moteurs un par un

    """
    def GenerateVirtualSpeed(self):
        #détermination des consignes d'avance et de rotation
        deltaX = self.TgtX - self.position.X
        deltaY = self.TgtY - self.position.Y
        self.Distance = sqrt(deltaX*deltaX + deltaY*deltaY)
        #selon le type, on définit la distance et l'angle restant
        if self.Type == 'Polar':
            if (self.Distance > DISTANCE_CONVERGENCE):
                absAngle = Rad2Deg(asin (deltaY/self.Distance))
                if (self.TgtX < self.position.X):
                    absAngle = AngleNorm(180-absAngle)
            else:
                absAngle = self.position.angle
            self.DeltaAngle = AngleNorm(absAngle-self.position.angle)

            #self.Distance = 50
        elif self.Type == 'Nul':
            self.Distance = 25
        #print('a =', str(self.Angle))
        # puis les consignes d'avance et de rotation
        self.SpdAvCns = 3*self.Distance #le PID
        self.SpdRotCns = 5*self.DeltaAngle #le PID
        #print('sys = ',sys.path)
        #Determination de la convergence
        self.Converge = False
        if self.Type == 'Polar' and self.Distance < DISTANCE_CONVERGENCE:
            self.Converge = True
        if self.Type == 'Rotation' and self.DeltaAngle < ANGLE_CONVERGENCE:
            self.Converge = True
    def DriveWheels(self):
        #d�termination des consignes droite et gauche et pilotage des moteurs
        if self.Type == 'Nul':
            self.SpdWhlRightCns=0
            self.SpdWhlLeftCns=0
        elif self.Type == 'Manu':
            self.SpdWhlLeftCns = self.ManuLeft
            self.SpdWhlRightCns = self.ManuRight
        else:  #cas Polaire ou Polaire arrière
            #on peut appliquer une rampe et des saturation
            self.SpdWhlLeftCns=self.SpdAvCns-self.SpdRotCns
            self.SpdWhlRightCns=self.SpdAvCns+self.SpdRotCns
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
        self.DeltaAngle = 0
        self.SpdAvCns = 0
        self.SpdRotCns = 0
        self.SpdWhlRightCns = 0
        self.SpdWhlLeftCns=0
        self.ManuLeft=0
        self.ManuRight=0
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
