# -*-coding:Latin-1 -*
import sys
import os

from Definitions import *
from math import sqrt, asin
#from Definitions import AngleNorm
#if sys.platform != 'win32':
#from ev3dev2.motor import OUTPUT_B
from  ev3dev2.motor import OUTPUT_B, OUTPUT_A, LargeMotor
from ev3dev2 import get_current_platform

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
        elif self.Type == 'Rotation':
            self.DeltaAngle = AngleNorm(self.TgtAlpha-self.position.angle)
            self.Distance = 0
        elif self.Type == 'Nul':
            self.Distance = 0
        # puis les consignes d'avance et de rotation
        if abs(self.DeltaAngle) > 30: #on est trop tourné, il faut se mettre dans l'axe d'abord
            #TODO mettre une carto pour le coef Distance, en fonction de l'angle
            self.SpdAvCns = 0
        elif abs(self.DeltaAngle) > 15: # on est pas loin de l'axe, on avance quand même
            self.SpdAvCns = KP_AVANCE*self.Distance*(2-2*self.DeltaAngle/300)
        else:#on est quasi dans l'axe, on avance
            self.SpdAvCns = KP_AVANCE*self.Distance
        self.SpdRotCns = KP_ROTATION*self.DeltaAngle

        #saturation des vitesses
        #TODO : définir si besoin d'une vitesse max négative pour l'avance
        self.SpdAvCns = max(-self.SpdAvMax, min(self.SpdAvMax,self.SpdAvCns))
        self.SpdRotCns = max(-self.SpdRotMax, min(self.SpdRotMax,self.SpdRotCns))
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
        # Pilotage des moteurs
        print('commande = ', str(self.SpdWhlRightCns))
        if self.platform != 'fake':
            self.MotorRight.speed_sp = -self.SpdWhlRightCns
            self.MotorLeft.speed_sp = -self.SpdWhlLeftCns
            self.MotorRight.run_forever()
            self.MotorLeft.run_forever()
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
        self.SpdAvMax = 100
        self.SpdRotMax = 100
        self.SpdWhlRightCns = 0
        self.SpdWhlLeftCns=0
        self.ManuLeft=500
        self.ManuRight=500
        self.Blocage = False
        self.TgtX = 0
        self.TgtY = 0
        self.TgtAlpha = 0
        self.Type = 'Nul';
        self.position = pos
        self.robot=rob
        #self.Type = MOVE_NUL
        self.platform = get_current_platform()
        if self.platform != 'fake':
            self.MotorRight = LargeMotor(OUTPUT_A)
            self.MotorLeft = LargeMotor(OUTPUT_B)
            self.MotorLeft.run_forever()
            self.MotorRight.run_forever()

if __name__ == "__main__":
    a=Asserv()
    print('blocage vaut :',a.Blocage)
    a.DetermineBlocage()
    print('blocage vaut :',a.Blocage)
    a.DetermineBlocage()
    print('blocage vaut :',a.Blocage)
