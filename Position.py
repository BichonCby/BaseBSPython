# -*-coding:Latin-1 -*
#import Robot
#from Definitions import robot
import Definitions

from math import cos, sin, pi
#sensor.Tirette

class Position:
    """ Classe permettant de calculer la position du robot à partir de ses codeurs, ou d'ailleurs
    la fonction principale est CalculPosition
    Mais d'autres fonctions peuvent permette de récupérer la position, la vitesse, etc...
    """
    def __init__(self,rob,sens):
        """Valeur d'init
        X et Y sont en mm, en position absolue par rapport au terrain
        angle est en degré (flottant) absolu (non relatif)
        """
        self.robot=rob
        self.sensorMgt=sens
        self.EncoderRightOld = 0
        self.EncoderLeftOld = 0
        # on déclare les variables de la classe
        self.X = 300.0
        self.Y = 400.0
        self.angle = 0.0
        self.init = True

    def CalculPosition(self):
        # Tous les calculs sont fait ici ou dans des sous fonctions, invisibles par le reste du programe
        # A la fin de la fonction, on dot avoir un nouveau X, Y et angle
        # on calcule aussi une vitesse brute (ou pas)
        self.sensorMgt.ReadEncoder()
        #print(str(self.sensorMgt.EncoderRight))
        if self.init == True:
            self.init=False
            deltaRight = 0
            deltaLeft = 0
        else:
            deltaRight = self.sensorMgt.EncoderRight - self.EncoderRightOld
            deltaLeft = self.sensorMgt.EncoderLeft - self.EncoderLeftOld

        if deltaRight > 180:#débordement
            deltaRight -= 360
        elif deltaRight < -180:
            deltaRight += 360
        if deltaLeft > 180:#débordement
            deltaLeft -= 360
        elif deltaLeft < -180:
            deltaLeft += 360
        CONV_DELTA_ANGLE = 6.32
        delta = (deltaRight-deltaLeft)/CONV_DELTA_ANGLE
        self.angle +=delta
        #normalisation de l'angle entre -180 et 180
        if self.angle <= -180.0:
            self.angle += 360.0
        elif self.angle > 180.0:
            self.angle -= 360.0
        self.angleRad = self.angle*pi/180
        #calcul des X et Y
        CONV_MM = 0.1737
        deltaX = (deltaRight+deltaLeft)*cos((self.angle-delta/2)*pi/180)*CONV_MM
        self.X += deltaX
        deltaY = (deltaRight+deltaLeft)*sin((self.angle-delta/2)*pi/180)*CONV_MM
        self.Y += deltaY
        #mémorisation des positions des capteurs
        self.EncoderLeftOld = self.sensorMgt.EncoderLeft
        self.EncoderRightOld = self.sensorMgt.EncoderRight

    def SetPosition(self,x=-1000,y=-1000,angle=-1000):
        # red�finit la position du robot, par exemple suite � un recalage
        # Attention toutefois � la couleur !!!!
        if x!= -1000:
            self.X = x
        if y!= -1000:
            self.Y = y
        if angle != -1000:
            self.angle = angle
        if self.robot.Color == 'blue':
            self.X = -self.X

# test de la classe
if __name__ == "__main__":
    p=Position()
    print('X vaut :',p.X)
    p.CalculPosition()#evolution
    print('X / Y vaut :',p.X, p.Y)
    #recalage sur les X par exemple
    p.SetPosition(x=200,angle=90)
    print('X / Y vaut :',p.X, p.Y)
    #recalage sur les Y par exemple
    p.SetPosition(y=200,angle=-90)
    print('X / Y vaut :',p.X, p.Y)
