"""
    Script qui lit toutes les lignes où la latitude et la longitude ne sont pas à jour, et regarde l'adresse, 
    si elle est vide on laisse la latitude et la longitude, sinon on récupère la latitude et la longitude grâce à mapQuest
    Fonctionne avec un proxy
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
        if(row[2] == ""): # S'il n'y a pas d'adresse
            # On ne change pas la latitude et la longitude mais on met miseAJour à 1
            cursorUpdate.execute("UPDATE installation SET misAJour=1 WHERE numInst="+str(row[0])+";")
        else: # Sinon
            
            location = row[2]+" "+row[3]+" France" # On prend adresse + ville + France

            # On cherche la latitude et la longitude de l'adresse
            urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
            proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'    
            url = 'https://www.mapquestapi.com/geocoding/v1/address?' + urlencode(urlParams)
            req = urlrequest.Request(url)
            req.set_proxy(proxy_host, 'http')
            response = urlrequest.urlopen(req)
            
            data = response.read().decode('utf8')
            jsonData = json.loads(str(data))
            response.close()
            latitude = str(jsonData['results'][0]['locations'][0]['latLng']['lat'])
            longitude = str(jsonData['results'][0]['locations'][0]['latLng']['lng'])

            # 
            location = latitude+","+longitude

            urlParams = {'location': location, 'key': API_KEY, 'outFormat':'json'}
            
            url = 'https://www.mapquestapi.com/geocoding/v1/reverse?' + urlencode(urlParams)
            req = urlrequest.Request(url)
            req.set_proxy(proxy_host, 'http')
            response = urlrequest.urlopen(req)

            data = response.read().decode('utf8')
            jsonData = json.loads(str(data))

except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    connBd.commit()
    cursorSelect.close()
    cursorUpdate.close()
    connBd.close()
