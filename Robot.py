# -*-coding:Latin-1 -*
from ev3dev2  import get_current_platform
from Definitions import *


if get_current_platform() == CIBLE:
    from ev3dev2.display import Display
    import ev3dev2.fonts as fonts


#from GR2020 import robot
class Robot:
    """ Classe qui va g�re les robot, se particularit�s, et le match aussi
    on va avoir les dimension (utile?) la couleur, le temps de match...
    """

    def __init__(self):
        #valeurs d'init
        self.Color='blue'
        self.Largeur = 300
        self.Longueur = 430
        self.Recalage = 170
        self.MatchEnCours = False
        self.Score = 10
        self.StepTime = 0.02 # pas de calcul de la s�quence
        self.platform = get_current_platform()
        if self.platform == CIBLE:
            self.display = Display()
            self.myfont = fonts.load('charBI24')
    def SetColor(self,coul):
        if coul == 'blue' or coul == 'yellow':
            self.Color = coul
        else:
            print('S�rieux?, mais tu connais pas les couleurs de cette ann�e ou quoi???')
    def DisplayScore(self):
        if self.platform == CIBLE:
            #self.display.clear()
            txt = 'score'
            #self.display.text_grid(txt,False,2,1,font=self.myfont)
            #self.display.update()
            #print('score = ',self.Score)
        pass
    def DisplayPos(self,x,y,alpha):
        if self.platform == CIBLE:
            self.display.clear()
            txt = 'x='+str(int(x))
            self.display.text_grid(txt,False,2,1,font=self.myfont)
            txt = 'y='+str(int(y))
            self.display.text_grid(txt,False,2,3,font=self.myfont)
            txt = 'a='+str(int(alpha))
            self.display.text_grid(txt,False,2,5,font=self.myfont)
            self.display.update()
            pass


#Test de la classe
if __name__ == "__main__":
    r=Robot()
    print('couleur vaut :',r.Color)
    r.SetColor('yellow')
    print('couleur vaut :',r.Color)
    r.SetColor('green')
    print('couleur vaut :',r.Color)
    print('Longueur vaut :',r.Longueur)
