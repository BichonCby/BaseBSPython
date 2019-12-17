# -*-coding:Latin-1 -*
""" fonctions de la stratégie"""
#import Asserv
#from .context import asserv
#from  Definitions import *
#from GR2020 import asserv

class MoveManager:
	""" Classe qui va gérer les deplacements
	...
	"""
	
	def __init__(self,ass):
		#valeurs d'init
		self.asserv = ass
		
	def GoFor(self,x,y,tmin,tmax):
		pass
		self.asserv.TgtX = x
	
	
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
