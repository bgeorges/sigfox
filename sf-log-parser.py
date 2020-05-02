import json
import csv
import http.client

viper = "viper-oyster.4b63.pro-ap-southeast-2.openshiftapps.com"
logs = "data/logs.csv"
connection = http.client.HTTPConnection(viper)

with open(logs, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    print("Device\tDate\tCoordinates\tSpeed")
    for row in reader:
        payload = row[5]
        device = row[6]
        d = row[11]
        connection.request("GET", "/parse/"+payload)
        response = connection.getresponse()
        data = response.read()
        j = json.loads(data)
        if 'Longitude' in j:
            speed = j["SpeedKmH"]
            coord = "{},{}".format(j["Latitude"], j["Longitude"])
            print("{}\t{}\t{}\t{}".format(
                device, d, coord, speed))
connection.close()
