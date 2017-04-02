from lib.bottle import route, static_file, run, template

import json

from services.activities.ActivityService import allActivities, lesVillesActivite, lesInstallationsVille

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/villeActivity/<numeroActivite>')
def afficherVille(numeroActivite):
	villes = lesVillesActivite(numeroActivite)
	jsonActivities = []
	for ville in villes:
		jsonActivities.append(ville.__dict__)
	return { "villes" : jsonActivities }

@route('/installationsVille/<numAct>/<ville>')
def afficherInstallation(numAct, ville):
	installations = lesInstallationsVille(numAct, ville)
	jsonActivities = []
	for installation in installations:
		jsonActivities.append(installation.__dict__)
	return { "installations" : jsonActivities }

@route('/activities')
def activities():
	activities = allActivities()
	jsonActivities = []
	for activity in activities:
		jsonActivities.append(activity.__dict__)
	return { "activities" : jsonActivities }

@route('/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./html')

run(host='localhost', port=8888)