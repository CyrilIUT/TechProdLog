import csv


with open('CSV/installations_table.csv', newline='') as csvfile:
	readerInstallation = csv.DictReader(csvfile)
	for row in readerInstallation:
		print("Numéro : "+row['Numéro de l\'installation']+"\n")
		print("Nom : "+row['Nom usuel de l\'installation']+"\n")
		print("Adresse : "+row['Numero de la voie']+" "+row['Nom de la voie']+"\n")
		print("Code postal : "+row['Code postal']+"\n")
		print("Ville : "+row['Nom de la commune']+"\n")
		print("Latitute : "+row['Latitude']+"\n")
		print("Longitude : "+row['Longitude']+"\n")
		
		print("\n\n\n")

with open('CSV/equipements.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print("Numéro : "+row['EquipementId']+"\n")
		print("Nom : "+row['EquNom']+"\n")
		print("Numéro de l'installation : "+row['InsNumeroInstall'])
		print("\n\n\n")


with open('CSV/equipements_activites.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print("Numéro activité : "+row['ActCode']+"\n")
		print("Nom activité : "+row['ActLib']+"\n")
		print("Numéro de l'equipement : "+row['EquipementId'])
		print("\n\n\n")
