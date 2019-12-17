# -*-coding:Latin-1 -*
""" fonctions de la stratégie"""
import MoveManager
import time
from threading import Thread

def InitRobot():
	pass
	

class MatchRobot(Thread):
	""" Tread chargé de glancer les fonctions récurrentes"""
	
	def __init__(self,ass):
		Thread.__init__(self)
		self.asserv=ass
		self.m=MoveManager.MoveManager(ass)
				
	def run(self):
		""" Le code à executer quand le thread est lancé """	
		self.m.GoFor(100,200,10,1000)
		time.sleep(0.5)
		self.m.GoFor(300,200,10,1000)
		#self.asserv.TgtX = 120
		#ActivateDoor()