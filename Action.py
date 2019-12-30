# -*-coding:Latin-1 -*
#from Definitions import LOCK_UNLOCK,LOCK_NEW,LOCK_LOCK
from Definitions import *

class Action:
	""" Classe qui va gérer les actionneurs hors propulsion
	...
	"""
	
	def __init__(self,rob,sens):
		#valeurs d'init
		self.StateDoor = 0 #état actuel de la porte
		self.StateDoorReq = 0 # état demandé par la strategie
		self.CntDoor = 0 # compteur utilisé dans la machine d'état de la porte
		self.robot=rob
		self.sensor=sens
		
		#self.lock = LOCK_UNLOCK
		
	def ActionState(self):
		#if self.lock == LOCK_NEW:
		#	self.StateDoor=self.StateDoorReq
		#	self.lock = LOCK_UNLOCK
		if self.StateDoor == 0:
			#on arrête le moteur
			pass
		elif self.StateDoor == 1:
			#on lance le moteur et on commence à compter
			self.CntDoor+=1
			if CntDoor > 5:
				self.StateDoor = 2
			pass
		elif sef.StateDoor == 2:
			pass
		else:
			pass
	def OpenDoor(self):
		#self.lock=LOCK_MODIFY
		#self.StateDoorReq = DOOR_OPEN
		#self.lock=LOCK_NEW
		pass
#Test de la classe		
if __name__ == "__main__":
	s=Sensor()
	print('Tirette =',s.Tirette)
	print('Bouton =',s.bouton)
	s.LectureTCHMUX()
	print('Bouton =',s.bouton)
