"""
    Script qui recupere les lignes non mise à jour (c'est à dire là où la latitude et longitude sont fausses),
    récupère la latitude et longitude de la ville et met à jour la BD
    Fonctionne avec un proxy
"""

import http.client
from urllib import request as urlrequest
from urllib.parse import urlencode
import json
import sqlite3

API_KEY = "sW3AW9ZdHwL01qxlAr1iYA8SAqEKQ9fr"

try:
    connBd = sqlite3.connect('../BD/instalPdll.db')
    cursorSelect = connBd.cursor()
    cursorUpdate = connBd.cursor()
    cursorSelect.execute("SELECT numInst,ville FROM installation WHERE misAJour=0;")
    for row in cursorSelect:
        location = row[1]+" France"

        urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
        proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'    # host and port of your proxy
        url = 'https://www.mapquestapi.com/geocoding/v1/address?' + urlencode(urlParams)
        req = urlrequest.Request(url)
        req.set_proxy(proxy_host, 'http')
        response = urlrequest.urlopen(req)
        
        data = response.read().decode('utf8')
        jsonData = json.loads(str(data))
        response.close()

        latitude = str(jsonData['results'][0]['locations'][0]['latLng']['lat'])
        longitude = str(jsonData['results'][0]['locations'][0]['latLng']['lng'])
        cursorUpdate.execute("UPDATE installation SET latitude="+latitude+", longitude="+longitude+", misAJour=1 WHERE numInst="+str(row[0])+";")

except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    connBd.commit()
    cursorSelect.close()
    cursorUpdate.close()
    connBd.close()
