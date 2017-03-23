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
			values = (row["Numéro de l'installation"], row["Nom usuel de l'installation"], (row['Numero de la voie']+" "+row['Nom de la voie']), row['Code postal'], row['Nom de la commune'], row['Latitude'], row['Longitude'])
			cursor.execute('''INSERT INTO installation values(?,?,?,?,?,?,?)''',values)

with open('CSV/equipements_activites.csv',newline='') as csvfile:
	readerInstallation = csv.DictReader(csvfile)
	for row in readerInstallation:
		if(row['ActCode'] != ''):
			if(row['ActLib'] == ''):
				values = (row['ActCode'],"Indefini")
			else:
				values = (row['ActCode'],row['ActLib'])

			cursor.execute("SELECT * FROM activite where numAct =\'"+row['ActCode']+"\';")
			row = cursor.fetchone()
			
			if row is None:
				cursor.execute('''INSERT INTO activite values (?,?)''',values)

conn.commit()
