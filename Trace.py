import time
from ev3dev2 import get_current_platform

class Trace:
    def __init__(self):
        try:
            if get_current_platform() == 'ev3':
                fic=open('num','r')
            else:
                fic=open('numPC','r')
            num = int(fic.read())
            fic.close()
        except:
            num=0
        num=num+1
        if get_current_platform() == 'ev3':
            fic = open('num','w')
        else:
            fic = open('numPC','w')
        fic.write(str(num))
        fic.close()
        if get_current_platform() == 'ev3':
            txt='LogBrickStoryGR_%0.5d' % num +'.log'
        else:
            txt='LogBrickStoryGRPC_%0.5d' % num +'.log'
        #txt = 'toto'
        print('fichier =', txt)
        self.fichier = open(txt,'w')
    def Log(self,texte):
        self.fichier.write(texte)
    def Close(self):
        print('fermeture du fichier')
        self.fichier.close()
