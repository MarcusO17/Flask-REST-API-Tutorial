from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#Make Class with Resource
class HelloWorld(Resource):
    def get(self):
        return {"data":"Hello World"}
    

api.add_resource(HelloWorld, "/helloworld")


if __name__ == "__main__":
    #Start App Server and Flask App, With Debug Mode (Log Info)
    app.run(debug=True)