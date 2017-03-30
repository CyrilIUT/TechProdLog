"""
    Script qui lit toutes les lignes pour récuperer la latitude et la longitude, et regarde grâce à mapquest
    si l'adresse est dans Pays de la Loire, si elle y est, on ne change rien, sinon on laisse "misAJour" à 0
    Fonctionne avec un proxy
"""

import http.client
from urllib import request as urlrequest
from urllib.parse import urlencode
import json
import sqlite3

API_KEY = "aamApwdh5AeQ00c6uZYGy8l4bl8JU28T"

try:
    connBd = sqlite3.connect('../BD/instalPdll.db')
    cursorSelect = connBd.cursor()
    cursorUpdate = connBd.cursor()
    cursorSelect.execute("SELECT latitude, longitude, numInst FROM installation WHERE misAJour=0")
    for row in cursorSelect:
        
            location = str(row[0])+","+str(row[1])

            urlParams = {'location': location, 'key': API_KEY, 'outFormat':'json'}
            proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'    # host and port of your proxy
            url = 'https://www.mapquestapi.com/geocoding/v1/reverse?' + urlencode(urlParams)
            req = urlrequest.Request(url)
            req.set_proxy(proxy_host, 'http')
            response = urlrequest.urlopen(req)
            
            data = response.read().decode('utf8')
            jsonData = json.loads(str(data))
            response.close()
            
            region = str(jsonData['results'][0]['locations'][0]['adminArea3'])
            print(str(row[2])+" : "+region)
            if(region == "Pays de la Loire"):
                cursorUpdate.execute("UPDATE installation SET misAJour=1 WHERE numInst="+str(row[2])+";")
            else:
                print(" : A changer")
            
            
except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    connBd.commit()
    cursorSelect.close()
    cursorUpdate.close()
    connBd.close()
