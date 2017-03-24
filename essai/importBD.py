import csv, sqlite3

conn = sqlite3.connect('instalPdll.db')
cursor = conn.cursor()

with open("CSV/equipements.csv", newline='') as csvfile:
	readerInstallation = csv.DictReader(csvfile)
	for row in readerInstallation:
		values = (row['EquipementId'], row['EquNom'], row['InsNumeroInstall'])
		cursor.execute('''INSERT INTO equipement values (?,?,?)''',values)


with open('CSV/installations_table.csv', newline='') as csvfile:
	readerInstallation = csv.DictReader(csvfile)
	for row in readerInstallation:
		liste = row['Nom de la voie'].split(' ')
		if("D" in liste or "d" in liste):
			values = (row["Numéro de l'installation"], row["Nom usuel de l'installation"], row['Nom du lieu dit'], row['Code postal'], row['Nom de la commune'], row['Latitude'], row['Longitude'], 0)
		else:
			if(row['Nom de la voie'] == ''):
				values = (row["Numéro de l'installation"], row["Nom usuel de l'installation"], row['Nom du lieu dit'], row['Code postal'], row['Nom de la commune'], row['Latitude'], row['Longitude'], 0)
			elif(row['Numero de la voie'] == '' and row['Nom de la voie'] != ''):
				values = (row["Numéro de l'installation"], row["Nom usuel de l'installation"], row['Nom de la voie'], row['Code postal'], row['Nom de la commune'], row['Latitude'], row['Longitude'], 0)
			else:
				values = (row["Numéro de l'installation"], row["Nom usuel de l'installation"], (row['Numero de la voie']+' '+row['Nom de la voie']), row['Code postal'], row['Nom de la commune'], row['Latitude'], row['Longitude'], 0)

		cursor.execute('''INSERT INTO installation values(?,?,?,?,?,?,?,?)''',values)

with open('CSV/equipements_activites.csv',newline='') as csvfile:
	readerInstallation = csv.DictReader(csvfile)
	for row in readerInstallation:
		if(row['ActCode'] != ''):
			donnes = (row['EquipementId'],row['ActCode'])
			if(row['ActLib'] == ''):
				values = (row['ActCode'],"Indefini")
			else:
				values = (row['ActCode'],row['ActLib'])

			cursor.execute("SELECT * FROM activite where numAct =\'"+row['ActCode']+"\';")
			ligne = cursor.fetchone()

			if ligne is None:
				cursor.execute('''INSERT INTO activite values (?,?)''',values)

			cursor.execute("SELECT * FROM liaisonEquAct where numAct =\'"+row['ActCode']+"\' and numEqu =\'"+row['EquipementId']+"\';")
			ligne2 = cursor.fetchone()

			if ligne2 is None:
				cursor.execute('''INSERT INTO liaisonEquAct values (?,?)''',donnes)

conn.commit()
