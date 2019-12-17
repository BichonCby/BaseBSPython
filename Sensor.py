# -*-coding:Latin-1 -*

class Sensor:
	""" Classe qui va gérer les capteurs
	...
	"""
	
	def __init__(self):
		#valeurs d'init
		self.Tirette=True
		self.BAU = False
		self.bouton=True
		self.EncoderRight = 0
		self.EncoderLeft = 0
		
	def LectureTCHMUX(self):
		self.bouton = False
	def ReadEncoder(self):
		#lecture des capteurs de rotation pour la position
		self.EncoderRight = 1
		self.EncoderLeft = 1
		
#Test de la classe		
if __name__ == "__main__":
	s=Sensor()
	print('Tirette =',s.Tirette)
	print('Bouton =',s.bouton)
	s.LectureTCHMUX()
	s.ReadEncoder()
	print('Bouton =',s.bouton)
