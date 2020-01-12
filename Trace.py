import time
class Trace:
    def __init__(self):
        txt='logGR_'+time.strftime("%Y%m%d_%H%M%S") +'.log'
        #txt = 'toto'
        print('fichier =', txt)
        self.fichier = open(txt,"x")
    def Log(self,texte):
        self.fichier.write(texte)
    def Close(self):
        self.fichier.close()
