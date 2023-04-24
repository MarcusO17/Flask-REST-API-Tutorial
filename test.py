import requests

BASE = "http://127.0.0.1:5000/"

params = {"name": "APIFLASK", "views": 10299, "likes":100}
response = requests.put(BASE+"video/2", params)
print(response.json())
input() # Pause
response = requests.get(BASE+"video/1", params)
print(response.json())