# -*-coding:Latin-1 -*
""" fonctions de la strat�gie"""
import time
from threading import Thread
#global mov
from Definitions import *

def InitRobot():
    #print('movinit = ',mov.id)
    pass


class MatchRobot(Thread):
    """ Tread charg� de lancer les fonctions r�currentes"""

    def __init__(self,mov,ass,rob,action):
        Thread.__init__(self)
        #self.m=MoveManager.MoveManager()
        self.m = mov
        self.a = ass
        self.r = rob
        self.act = action
        #print('mov = ',self.m.id)
    def run(self):
        """ Le code � executer quand le thread est lanc� """
        # cette fonction pourra �tre un s�quenceur intelligent
        #Pour l'instant, il ne g�re qu'une s�quence constante
        self.ActivateMachin()
        self.VaChercherBonheur()

    def ActivateMachin(self):
        self.m.GoFor(100,200,10,1000)
        time.sleep(0.5)
        self.m.GoBack(300,200,10,1000)
    def VaChercherBonheur(self):
        self.act.OpenDoor('Right')
        self.m.DontMove(100)
