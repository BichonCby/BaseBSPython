# -*-coding:Latin-1 -*
""" fonctions de la strat�gie"""
#import Asserv
#from .context import asserv
from  Definitions import *
import time
#from GR2020 import asserv
#
class MoveManager:
    """ Classe qui va gérer les deplacements
    ...
    """

    def __init__(self,ass,rob):
        #valeurs d'init
        self.id = 'move'
        self.a=ass
        self.robot=rob
        pass
    def GoFor(self,x,y,tmin,tmax):
        #on va au point d�termin� en marche avant
        pass
        self.a.TgtX = x
        self.a.TgtY = y
        self.a.Type = 'Polar'
        top = time.time()
        #while time.time()-top <tmin:
        #    pass #on attend le temps min de toute façon. ajouter la détection, non?
        while self.a.Converge == False and time.time()-top < tmax:
            pass # on attend la convergence ou le temps max
    def GoBack(self,x,y,tmin,tmax):
        #on va au point d�termin�, en marche arri�re
        pass  #a compl�ter
    def DontMove(self,tmin):
        #on ne bouge pas
        self.a.Type = 'Nul'
    def Rotate(self,acible):
        self.a.Type = 'Rotation'
        self.a.TgtAlpha = acible
        while self.a.Converge == False:
            pass # on attend la convergence ou le temps max
    def MoveManu(self,speed,tmax):
        self.a.Type= 'Manu'
        self.a.ManuLeft = speed
        self.a.ManuRight = speed

        """ Lock
        Type_depl = AV
        cibleX=x
        CibleY=y
        Unlock
        Top=time.time()

        While (not convergence and not tmax)
        If detection
            Avoid() #on attend d'avoir fini
            Lock
            Type_depl
            x,y,
            top=time.time()
        If tmax
            Return -1
        Time.sleep(0.02)
        % on attend le temps mini
        While(time.time()-top<tmin)
            Time.sleep(0.02)
        """
