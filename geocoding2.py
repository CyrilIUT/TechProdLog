import http.client
from urllib import request as urlrequest
from urllib.parse import urlencode
import json
import sqlite3

API_KEY = "aamApwdh5AeQ00c6uZYGy8l4bl8JU28T"

try:
    connBd = sqlite3.connect('instalPdll.db')
    cursorSelect = connBd.cursor()
    cursorSelect.execute("SELECT latitude, longitude, numInst FROM installation")
    for row in cursorSelect:
        
            location = str(row[0])+","+str(row[1])

            """ Avec un proxy on utilise ces lignes là
            """
            urlParams = {'location': location, 'key': API_KEY, 'outFormat':'json'}
            proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'    # host and port of your proxy
            url = 'https://www.mapquestapi.com/geocoding/v1/reverse?' + urlencode(urlParams)
            req = urlrequest.Request(url)
            req.set_proxy(proxy_host, 'http')
            response = urlrequest.urlopen(req)
            
            data = response.read().decode('utf8')
            jsonData = json.loads(str(data))
            response.close()
            """

            urlParams = {'location': location, 'key': API_KEY, 'outFormat':'json'}
            url = "/geocoding/v1/reverse?" + urlencode(urlParams)

            conn = http.client.HTTPConnection("www.mapquestapi.com")
            conn.request("GET", url)

            res = conn.getresponse()
            print(res.status, res.reason)
            print("\n\n\n")
            data = res.read()
            jsonData = json.loads(data)
            conn.close()
            """

            region = str(jsonData['results'][0]['locations'][0]['adminArea3'])
            if(region != "Pays de la Loire"):
                print(str(row[2])+" : "+region+"\n")
            
            
except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    
    cursorSelect.close()
    connBd.close()
