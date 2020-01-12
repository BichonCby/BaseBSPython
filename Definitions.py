# -*-coding:Latin-1 -*
""" les #define en python, c'est ici que ca se passe"""
from math import pi

''' Constantes de machines à état d'actionneurs'''
LOCK_NEW = 0
LOCK_UNLOCK = 1
LOCK_LOCK = 2

DOOR_OPEN = 0

''' Constantes d'asservissement'''
ANGLE_CONVERGENCE = 2
DISTANCE_CONVERGENCE = 20
KP_AVANCE = 6
KP_ROTATION = 50

''' Fonctions utilitaires
'''

def AngleNorm(a):
    return a
def Rad2Deg(a):
    return(a*180/pi)

