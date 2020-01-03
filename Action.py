# -*-coding:Latin-1 -*
#from Definitions import LOCK_UNLOCK,LOCK_NEW,LOCK_LOCK
from Definitions import *

class Action:
    """ Classe qui va g�rer les actionneurs hors propulsion
    ...
    """

    def __init__(self,rob,sens):
        #valeurs d'init
        self.StateDoor = 0 #�tat actuel de la porte
        self.StateDoorReq = 0 # �tat demand� par la strategie
        self.CntDoor = 0 # compteur utilis� dans la machine d'�tat de la porte
        self.robot=rob
        self.sensorMgt=sens

        #self.lock = LOCK_UNLOCK

    def ActionState(self):
        #if self.lock == LOCK_NEW:
        #    self.StateDoor=self.StateDoorReq
        #    self.lock = LOCK_UNLOCK
        if self.StateDoor == 0:
            #on arr�te le moteur
            pass
        elif self.StateDoor == 1:
            #on lance le moteur et on commence � compter
            self.CntDoor+=1
            if CntDoor > 5:
                self.StateDoor = 2
            pass
        elif sef.StateDoor == 2:
            pass
        else:
            pass
    def OpenDoor(self):
        #self.lock=LOCK_MODIFY
        #self.StateDoorReq = DOOR_OPEN
        #self.lock=LOCK_NEW
        pass
#Test de la classe
if __name__ == "__main__":
    s=Sensor()
    print('Tirette =',s.Tirette)
    print('Bouton =',s.bouton)
    s.LectureTCHMUX()
    print('Bouton =',s.bouton)
