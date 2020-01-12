# -*-coding:Latin-1 -*
from Definitions import *
from ev3dev2 import get_current_platform
if get_current_platform != 'fake':
    from ev3dev2.sensor import *
    from AddSensors import AngleSensor
    from ev3dev2.sensor.lego import TouchSensor

class SensorMgt:
    """ Classe qui va g�rer les capteurs
    ...
    """

    def __init__(self,rob):
        #valeurs d'init
        pass
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
            self.CapteurTirette = TouchSensor(INPUT_3)#pour les tests

    def ReadTCHMUX(self):
        self.bouton = False
        #print(str(self.CapteurTirette))
        if self.platform != 'fake':
            if self.CapteurTirette.value() == 1:
                self.Tirette = False
            else:
                pass
                self.Tirette = True
    def ReadEncoder(self):
        #lecture des capteurs de rotation pour la position
        if (self.platform != 'fake'):
            self.EncoderRight = self.EncoderSensRight.value()
            #inversion pour qu'en marche avant, les codeurs s'incrémente à droite et à gauche
            self.EncoderLeft = 360-self.EncoderSensLeft.value()
            pass

#Test de la classe
if __name__ == "__main__":
    r = 3
    s=SensorMgt(r)
    print('Tirette =',s.Tirette)
    print('Bouton =',s.bouton)
    s.ReadTCHMUX()
    s.ReadEncoder()
    print('Bouton =',s.bouton)
