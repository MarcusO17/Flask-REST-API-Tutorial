import requests

BASE = "http://127.0.0.1:5000/"

params = {"likes":10}
response = requests.put(BASE+"video/1", params)
print(response.json())