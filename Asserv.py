# -*-coding:Latin-1 -*

class Asserv:
	""" Classe qui va g�rer l'asservissement du robot.
	la fonction CalculAsserv va �tre appel�e de mani�re r�cursive par l'ext�rieur
	elle va faire appel � diff�rentes sous fonctions (g�n�ration trajectoire, etc..)
	la finalit� est de piloter les moteurs de propulsion (BO/BF)
	"""
	def GenerateVirtualSpeed(self):
		#d�termination des consignes d'avance et de rotation
		self.SpdAvCns+=1
	def DriveWheels(self):
		#d�termination des consignes droite et gauche et pilotage des moteurs
		self.SpdWhlRightCns+=1
		#print('Tgtx=',self.TgtX)
	def DetermineBlocage(self):
		#si la vitesse est nulle alors que la consigne ne l'est pas
		self.Blocage = not self.Blocage
	def CalculAsserv(self):
		#appel s�quentiel
		self.GenerateVirtualSpeed()
		self.DriveWheels()
	def __init__(self):
		self.Converge = False
		self.SpdAvCns = 0
		self.SpdRotCns = 0
		self.SpdWhlRightCns = 0
		self.SpdWhlLeftCns=0
		self.Blocage = False
		self.TgtX = 0
		self.TgtY = 0
		#self.Type = MOVE_NUL

if __name__ == "__main__":
	a=Asserv()
	print('blocage vaut :',a.Blocage)
	a.DetermineBlocage()
	print('blocage vaut :',a.Blocage)
	a.DetermineBlocage()
	print('blocage vaut :',a.Blocage)