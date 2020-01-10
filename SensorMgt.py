# -*-coding:Latin-1 -*
from Definitions import *
from ev3dev2.sensor import *
from AddSensors import AngleSensor

class SensorMgt:
    """ Classe qui va g�rer les capteurs
    ...
    """

    def __init__(self,rob):
        #valeurs d'init
        self.Tirette=True
        self.BAU = False
        self.bouton=True
        self.EncoderRight = 0
        self.EncoderLeft = 0
        self.robot = rob
        self.platform = get_current_platform()
        if (self.platform != 'fake'):
            self.EncoderSensRight = AngleSensor(INPUT_1)
            self.EncoderSensLeft = AngleSensor(INPUT_2)

    def ReadTCHMUX(self):
        self.bouton = False
    def ReadEncoder(self):
        #lecture des capteurs de rotation pour la position
        if (self.platform != 'fake'):
            self.EncoderRight = self.EncoderSensRight.value()
            #inversion pour qu'en marche avant, les codeurs s'incrémente à droite et à gauche
            self.EncoderLeft = 360-self.EncoderSensLeft.value()
            pass

#Test de la classe
if __name__ == "__main__":
    s=SensorMgt()
    print('Tirette =',s.Tirette)
    print('Bouton =',s.bouton)
    s.ReadTCHMUX()
    s.ReadEncoder()
    print('Bouton =',s.bouton)
