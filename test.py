import requests

BASE = "http://127.0.0.1:5000/"

params = "tim"
response = requests.get(BASE+"helloworld/"+ params)
print(response.json())