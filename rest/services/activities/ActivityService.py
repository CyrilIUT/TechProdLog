import sqlite3
from services.activities.Activity import Activity
from services.activities.Ville import Ville
from services.activities.Installation import Installation

def allActivities():
	activities = []

	connBd = sqlite3.connect('../BD/instalPdll.db')
	cursorSelect = connBd.cursor()
	cursorSelect.execute("SELECT numAct, nomAct FROM activite order by nomAct")
	for row in cursorSelect:
		activities.append(Activity(row[0], row[1]))
		
	connBd.close()
	return activities

def lesVillesActivite(numAct):
	villes = []
	connBd = sqlite3.connect('../BD/instalPdll.db')
	cursorSelect = connBd.cursor()
	cursorSelect.execute("SELECT ville, codePostal FROM installation i, equipement e, liaisonEquAct l, activite a WHERE a.numAct="+numAct+" AND i.numInst=e.numInst AND e.numEqu=l.numEqu AND l.numAct=a.numAct group by ville")
	for row in cursorSelect:
		villes.append(Ville(row[0], row[1]))
		
	connBd.close()
	return villes

def lesInstallationsVille(numAct, ville):
	installations = []
	connBd = sqlite3.connect('../BD/instalPdll.db')
	cursorSelect = connBd.cursor()
	cursorSelect.execute("SELECT i.numInst, i.nomInst, i.adresse, i.latitude, i.longitude FROM installation i, equipement e, liaisonEquAct l, activite a WHERE a.numAct="+numAct+" AND i.ville='"+ville+"' AND i.numInst=e.numInst AND e.numEqu=l.numEqu AND l.numAct=a.numAct")
	for row in cursorSelect:
		installations.append(Installation(row[0],row[1],row[2],row[3],row[4]))
		
	connBd.close()
	return installations
