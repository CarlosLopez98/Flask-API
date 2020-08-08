from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
			"carlos": {
				"age": 22, 
				"gender": "male"
			},
			"sergio": {
				"age": 26,
				"gender": "male"
			}

		}


class HelloWorld(Resource):
	def get(self, name):
		return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == '__main__':
	app.run(debug=True)