class Ville:
	def __init__(self, nom, codePostal):
		self.nom = nom
		self.codePostal = codePostal
		
	def __repr__(self):
		return "{} - {}".format(self.nom, self.codePostal)