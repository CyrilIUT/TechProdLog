import http.client
from urllib import request as urlrequest
from urllib.parse import urlencode
import json
import sqlite3

API_KEY = "sW3AW9ZdHwL01qxlAr1iYA8SAqEKQ9fr"

try:
    conn = sqlite3.connect('instalPdll.db')
    cursorSelect = conn.cursor()
    cursorUpdate = conn.cursor()
    cursorSelect.execute("SELECT numInst,nomInst,adresse,ville FROM installation WHERE latitude=0 AND longitude=0;")
    for row in cursorSelect:
        if(row[2] == " "):
            print(row[1]+" | "+row[3])
            location = row[1]+" "+row[3]
        else:
            print(row[2]+" | "+row[3])
            location = row[2]+" "+row[3]
        urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
        proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'    # host and port of your proxy
        url = 'https://www.mapquestapi.com/geocoding/v1/address?' + urlencode(urlParams)
        req = urlrequest.Request(url)
        req.set_proxy(proxy_host, 'http')
        response = urlrequest.urlopen(req)
        
        data = response.read().decode('utf8')
        jsonData = json.loads(str(data))
        latitude = str(jsonData['results'][0]['locations'][0]['latLng']['lat'])
        longitude = str(jsonData['results'][0]['locations'][0]['latLng']['lng'])
        cursorUpdate.execute("UPDATE installation SET latitude="+latitude+", longitude="+longitude+" WHERE numInst="+str(row[0])+";")
        response.close()
except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    conn.commit()
    cursorSelect.close()
    cursorUpdate.close()
    conn.close()
