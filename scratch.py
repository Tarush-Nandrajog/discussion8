import requests
import json
url = "https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today"
data1 = requests.get(url) 
data2 = data1.text 
data3 = json.loads(data2) 
data4 = json.dumps(data3)