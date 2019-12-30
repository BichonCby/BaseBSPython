# -*-coding:Latin-1 -*
#import Robot
#from Definitions import robot
import Definitions

from math import cos, sin, pi
#sensor.Tirette

class Position:
	""" Classe permettant de calculer la position du robot à partir de ses codeurs, ou d'ailleurs
	la fonction principale est CalculPosition
	Mais d'autres fonctions peuvent permette de récupérer la position, la vitesse, etc...
	"""
	def __init__(self,rob,sens):
		"""Valeur d'init
		X et Y sont en mm, en position absolue par rapport au terrain
		angle est en degré (flottant) absolu (non relatif)
		"""
		self.robot=rob
		self.sensor=sens
		# on déclare les variables de la classe
		self.X = 300.0
		self.Y = 450.0
		self.angle = 0.0
		
	def CalculPosition(self):
		# Tous les calculs sont fait ici ou dans des sous fonctions, invisibles par le reste du programe
		# A la fin de la fonction, on dot avoir un nouveau X, Y et angle
		# on calcule aussi une vitesse brute (ou pas)
		self.sensor.ReadEncoder()
		self.X -= 0.1
		self.Y += 0.01
		self.angle += 0.01
		self.angle = self.sensor.EncoderRight


	def SetPosition(self,x=-1000,y=-1000,angle=-1000):
		# redéfinit la position du robot, par exemple suite à un recalage
		# Attention toutefois à la couleur !!!!
		if x!= -1000:
			self.X = x
		if y!= -1000:
			self.Y = y
		if angle != -1000:
			self.angle = angle
		if self.robot.Color is 'blue':
			self.X = -self.X

# test de la classe
if __name__ == "__main__":
	p=Position()
	print('X vaut :',p.X)
	p.CalculPosition()#evolution
	print('X / Y vaut :',p.X, p.Y)
	#recalage sur les X par exemple
	p.SetPosition(x=200,angle=90)
	print('X / Y vaut :',p.X, p.Y)
	#recalage sur les Y par exemple
	p.SetPosition(y=200,angle=-90)
	print('X / Y vaut :',p.X, p.Y)