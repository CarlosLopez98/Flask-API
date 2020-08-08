import requests

BASE = "http://localhost:5000/"

response = requests.get(BASE + "helloworld/carlos")
print(response.json())