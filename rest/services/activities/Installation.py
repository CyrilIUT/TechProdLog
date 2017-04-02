class Installation:
	def __init__(self, code, nom, adresse, latitude, longitude):
		self.code = code
		self.nom = nom
		self.adresse = adresse
		self.latitude = latitude
		self.longitude = longitude


	def __repr__(self):
		return "{} - {} - {}".format(self.code, self.nom, self.adresse)