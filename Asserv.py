# -*-coding:Latin-1 -*

class Asserv:
	""" Classe qui va gérer l'asservissement du robot.
	la fonction CalculAsserv va être appelée de manière récursive par l'extérieur
	elle va faire appel à différentes sous fonctions (génération trajectoire, etc..)
	la finalité est de piloter les moteurs de propulsion (BO/BF)
	"""
	def GenerateVirtualSpeed(self):
		#détermination des consignes d'avance et de rotation
		self.SpdAvCns+=1
	def DriveWheels(self):
		#détermination des consignes droite et gauche et pilotage des moteurs
		self.SpdWhlRightCns+=1
		#print('Tgtx=',self.TgtX)
	def DetermineBlocage(self):
		#si la vitesse est nulle alors que la consigne ne l'est pas
		self.Blocage = not self.Blocage
	def CalculAsserv(self):
		#appel séquentiel
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