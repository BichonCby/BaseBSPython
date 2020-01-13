import time
class Trace:
    def __init__(self):
        try:
            fic=open('num','r')
            num = int(fic.read())
            fic.close()
        except:
            num=0
        num=num+1
        fic = open('num','w')
        fic.write(str(num))
        fic.close()
        txt='LogBrickStoryGR_%0.5d' % num +'.log'
        #txt = 'toto'
        print('fichier =', txt)
        self.fichier = open(txt,"x")
    def Log(self,texte):
        self.fichier.write(texte)
    def Close(self):
        self.fichier.close()
