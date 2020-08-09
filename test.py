import requests

BASE = "http://localhost:5000/"

data = [
	{"name": "Video 1", "views": 100, "likes": 10},
	{"name": "Video 2", "views": 1200, "likes": 150},
	{"name": "Video 3", "views": 300, "likes": 20}
]

for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())

response = requests.get(BASE + "video/2")
print(response.json())

response = requests.patch(BASE + "video/2", {"name": "Video nuevo 3"})
print(response.json())

response = requests.delete(BASE + "video/2")
print(response)