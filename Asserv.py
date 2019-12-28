# -*-coding:Latin-1 -*
from Definitions import *

class Asserv:
	""" Classe qui va gérer l'asservissement du robot.
	la fonction CalculAsserv va être appelée de manière récursive par l'extérieur
	elle va faire appel à différentes sous fonctions (génération trajectoire, etc..)
	la finalité est de piloter les moteurs de propulsion (BO/BF)
	"""
	def GenerateVirtualSpeed(self):
		#détermination des consignes d'avance et de rotation
		
		#selon le type, on définit la distance et l'angle restant
		if self.Type is 'Auto':
			self.Distance = 50
		elif self.Type is 'Nul':
			self.Distance = 25
		self.Angle = 5
		# puis les consignes d'avance et de rotation
		self.SpdAvCns = 3*self.Distance #le PID
		self.SpdRotCns = 5*self.Angle #le PID
		
		self.Converge = True
	def DriveWheels(self):
		#détermination des consignes droite et gauche et pilotage des moteurs
		self.SpdWhlRightCns+=1
		self.SpdWhlLeftCns+=2
		print('Tgtx=',self.TgtX)
	def DetermineBlocage(self):
		#si la vitesse est nulle alors que la consigne ne l'est pas
		#on peut faire un blocage par roue, ou en avance et rotation
		#il faut rajouter des temps des confirmation
		self.Blocage = not self.Blocage
	def CalculAsserv(self):
		#appel séquentiel
		self.GenerateVirtualSpeed()
		self.DriveWheels()
	def __init__(self,pos,rob):
		self.Converge = False
		self.Distance = 0 #distance restant à parcourir
		self.Angle = 0
		self.SpdAvCns = 0
		self.SpdRotCns = 0
		self.SpdWhlRightCns = 0
		self.SpdWhlLeftCns=0
		self.Blocage = False
		self.TgtX = 0
		self.TgtY = 0
		self.Type = 'Nul';
		self.position = pos
		self.robot=rob
		#self.Type = MOVE_NUL

if __name__ == "__main__":
	a=Asserv()
	print('blocage vaut :',a.Blocage)
	a.DetermineBlocage()
	print('blocage vaut :',a.Blocage)
	a.DetermineBlocage()
	print('blocage vaut :',a.Blocage)