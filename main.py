from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

videos
#Caching
videos = {}

class Video(Resource):
    #Create
    def get(self, videoID):
        return videos[videoID]
    
    #Add Data
    def put(self, videoID):
        return {}

api.add_resource(Video, "/video/<int:videoID>")

    
    
#<> shows params
#api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    #Start App Server and Flask App, With Debug Mode (Log Info)
    app.run(debug=True)