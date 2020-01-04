# -*-coding:Latin-1 -*
#from Definitions import LOCK_UNLOCK,LOCK_NEW,LOCK_LOCK
from Definitions import *

class Action:
    """ Classe qui va gérer les actionneurs hors propulsion
    ...
    """

    def __init__(self,rob,sens):
        #valeurs d'init
        self.StateRightDoor = 0 #�tat actuel de la porte
        self.StateDoorReq = 0 # �tat demand� par la strategie
        self.CntRightDoor = 0 # compteur utilis� dans la machine d'�tat de la porte
        self.StateLeftDoor = 0 #�tat actuel de la porte
        self.CntLeftDoor = 0 # compteur utilis� dans la machine d'�tat de la porte
        self.robot=rob
        self.sensorMgt=sens

        #self.lock = LOCK_UNLOCK

    def ActionState(self):
        #if self.lock == LOCK_NEW:
        #    self.StateDoor=self.StateDoorReq
        #    self.lock = LOCK_UNLOCK
        ## Porte droite
        if self.StateRightDoor == 'Stop':
            #on arr�te le moteur
            #TODO : arrêter le moteur
            pass
        elif self.StateRightDoor == 'Open':
            #on lance le moteur et on commence � compter
            #TODO : activer le moteur
            self.CntRightDoor+=1
            if self.CntRightDoor > self.CntDoorMax:
                self.StateRightDoor = 'Stop'
        elif self.StateRightDoor == 'Close':
            #on lance le moteur et on commence � compter
            #TODO : activer le moteur
            self.CntRightDoor+=1
            if self.CntRightDoor > self.CntDoorMax:
                self.StateRightDoor = 'Stop'
            pass
        else:
            pass
        ## Porte gauche
        if self.StateLeftDoor == 'Stop':
            #on arr�te le moteur
            #TODO : arrêter le moteur
            pass
        elif self.StateLeftDoor == 'Open':
            #on lance le moteur et on commence � compter
            #TODO : activer le moteur
            self.CntLeftDoor+=1
            if self.CntLeftDoor > self.CntDoorMax:
                self.StateLeftDoor = 'Stop'
        elif self.StateLeftDoor == 'Close':
            #on lance le moteur et on commence � compter
            #TODO : activer le moteur
            self.CntLeftDoor+=1
            if self.CntLeftDoor > self.CntDoorMax:
                self.StateLeftDoor = 'Stop'
            pass
        else:
            pass
        #TODO : voir si on gère la couleur ici ou en amont
    def OpenDoor(self, side):
        if side == 'Right':
            self.StateRightDoor = 'Open'
            self.CntRightDoor = 0
        if side == 'Left':
            self.StateLeftDoor = 'Open'
            self.CntLeftDoor = 0
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
