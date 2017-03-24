"""
    Script qui lit toutes les lignes où la latitude et la longitude ne sont pas à jour, et regarde l'adresse, 
    si elle est vide on laisse la latitude et la longitude, sinon on récupère la latitude et la longitude grâce à mapQuest
    Fonctionne sans proxy
"""

import http.client
from urllib import request as urlrequest
from urllib.parse import urlencode
import json
import sqlite3

API_KEY = "sW3AW9ZdHwL01qxlAr1iYA8SAqEKQ9fr"

try:
    connBd = sqlite3.connect('instalPdll.db')
    cursorSelect = connBd.cursor()
    cursorUpdate = connBd.cursor()
    cursorSelect.execute("SELECT numInst,nomInst,adresse,ville FROM installation WHERE misAJour=0;")
    for row in cursorSelect:
        if(row[2] == ""):#S'il n'y a pas d'adresse
            print(row[1]+" | "+row[3]+" : Je laisse la longitude et la latitude comme c'était")
            cursorUpdate.execute("UPDATE installation SET misAJour=1 WHERE numInst="+str(row[0])+";")
        else:
            print(row[2]+" | "+row[3]+" : Je mets à jour la latitude et la longitude")
            location = row[2]+" "+row[3]+" France"

            urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
            url = "/geocoding/v1/address?" + urlencode(urlParams)

            conn = http.client.HTTPConnection("www.mapquestapi.com")
            conn.request("GET", url)

            res = conn.getresponse()
            print(res.status, res.reason)
            print("\n\n\n")
            data = res.read()
            jsonData = json.loads(data)

            latitude = str(jsonData['results'][0]['locations'][0]['latLng']['lat'])
            longitude = str(jsonData['results'][0]['locations'][0]['latLng']['lng'])
            cursorUpdate.execute("UPDATE installation SET latitude="+latitude+", longitude="+longitude+", misAJour=1 WHERE numInst="+str(row[0])+";")
            conn.close()
except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    connBd.commit()
    cursorSelect.close()
    cursorUpdate.close()
    connBd.close()
