# -*-coding:Latin-1 -*

class Robot:
	""" Classe qui va g�re les robot, se particularit�s, et le match aussi
	on va avoir les dimension (utile?) la couleur, le temps de match...
	"""
	
	def __init__(self):
		#valeurs d'init
		self.Color='blue'
		self.Largeur = 300
		self.Longueur = 430
		self.Recalage = 170
		self.MatchEnCours = False
		self.Score = 10
		self.StepTime = 0.02 # pas de calcul de la s�quence
	def SetColor(self,coul):
		if coul == 'blue' or coul == 'yellow':
			self.Color = coul
		else:
			print('S�rieux?, mais tu connais pas les couleurs de cette ann�e ou quoi???')
	def DisplayScore(self):
		print('score = ',self.Score)
		pass
#Test de la classe		
if __name__ == "__main__":
	r=Robot()
	print('couleur vaut :',r.Color)
	r.SetColor('yellow')
	print('couleur vaut :',r.Color)
	r.SetColor('green')
	print('couleur vaut :',r.Color)
	print('Longueur vaut :',r.Longueur)