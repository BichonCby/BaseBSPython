# -*-coding:Latin-1 -*
from Definitions import *

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

    def ReadTCHMUX(self):
        self.bouton = False
    def ReadEncoder(self):
        #lecture des capteurs de rotation pour la position
        self.EncoderRight = 1
        self.EncoderLeft = 1

#Test de la classe
if __name__ == "__main__":
    s=SensorMgt()
    print('Tirette =',s.Tirette)
    print('Bouton =',s.bouton)
    s.ReadTCHMUX()
    s.ReadEncoder()
    print('Bouton =',s.bouton)
