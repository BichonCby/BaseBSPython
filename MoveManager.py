# -*-coding:Latin-1 -*
""" fonctions de la strat�gie"""
#import Asserv
#from .context import asserv
from  Definitions import *
#from GR2020 import asserv

class MoveManager:
	""" Classe qui va g�rer les deplacements
	...
	"""
	
	def __init__(self,ass,rob):
		#valeurs d'init
		self.id = 'move'
		self.a=ass
		self.robot=rob
		pass
	def GoFor(self,x,y,tmin,tmax):
		#on va au point d�termin� en marche avant
		pass
		self.a.TgtX = x
		self.a.TgtY = y
		self.a.Type = 'Auto'
	def GoBack(self,x,y,tmin,tmax):
		#on va au point d�termin�, en marche arri�re
		pass  #a compl�ter
	def DontMove(self,tmin):
		#on ne bouge pas
		self.a.Type = 'Nul'
	def Rotate(self,acible):
		self.a.Type = 'Rotation'
	def MoveManu(self,speed,tmax):
		self.a.Type= 'Manu'
		
		
		""" Lock
		Type_depl = AV
		cibleX=x
		CibleY=y
		Unlock
		Top=time.time()
		
		While (not convergence and not tmax)
		If detection
			Avoid() #on attend d'avoir fini
			Lock
			Type_depl
			x,y,
			top=time.time()
		If tmax
			Return -1
		Time.sleep(0.02)
		% on attend le temps mini
		While(time.time()-top<tmin)
			Time.sleep(0.02)
		"""
