# -*-coding:Latin-1 -*
""" fonctions de la stratégie"""
import time
from threading import Thread
#global mov
from Definitions import *

def InitRobot():
    #print('movinit = ',mov.id)
    pass


class MatchRobot(Thread):
    """ Tread chargé de lancer les fonctions récurrentes"""

    def __init__(self,mov,ass,rob,action):
        Thread.__init__(self)
        #self.m=MoveManager.MoveManager()
        self.m = mov
        self.a = ass
        self.r = rob
        self.act = action
        #print('mov = ',self.m.id)
    def run(self):
        """ Le code à executer quand le thread est lancé """
        # cette fonction pourra être un séquenceur intelligent
        #Pour l'instant, il ne gère qu'une séquence constante
        self.ActivateMachin()
        self.VaChercherBonheur()

    def ActivateMachin(self):
        self.m.GoFor(200,0,0.1,1000)
        #self.m.GoBack(300,200,10,1000)
        pass
    def VaChercherBonheur(self):
        #self.act.OpenDoor('Right')
        self.m.DontMove(100)
        pass
