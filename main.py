from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#Caching
names = {"marcus" : {"age" : 19, "gender": "male"},
         "tim" : {"age" : 27, "gender": "male"}}

#Make Class with Resource
# USING CRUD
class HelloWorld(Resource):
    #Read
    def get(self, name):
        return names[name]

    """#Create
    def post(self):
        return {"data":"Posted"}"""


    
    
#<> shows params
api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    #Start App Server and Flask App, With Debug Mode (Log Info)
    app.run(debug=True)