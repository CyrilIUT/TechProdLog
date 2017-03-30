import sqlite3

conn = sqlite3.connect('instalPdll.db')


cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS installation(
numInst INTEGER PRIMARY KEY,
nomInst TEXT,
adresse TEXT,
codePostal TEXT,
ville TEXT,
latitude NUMERIC,
longitude NUMERIC,
misAJour BOOLEAN)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS equipement(
numEqu INTEGER PRIMARY KEY,
nomEqu TEXT,
numInst INTEGER,
FOREIGN KEY(numInst) REFERENCES installation(numInst))""")

cursor.execute("""CREATE TABLE IF NOT EXISTS activite(
numAct INTEGER PRIMARY KEY,
nomAct TEXT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS liaisonEquAct(
numEqu INTEGER,
numAct INTEGER,
FOREIGN KEY(numEqu) REFERENCES equipement(numEqu),
FOREIGN KEY(numAct) REFERENCES activite(numAct),
PRIMARY KEY(numEqu,numAct)
)""")

conn.commit()
conn.close()