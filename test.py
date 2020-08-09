import requests

BASE = "http://localhost:5000/"

#response = requests.put(BASE + "video/1", {"name": "Video 1", "views": 100, "likes": 10})
#print(response.json())

response = requests.get(BASE + "video/6")
print(response.json())