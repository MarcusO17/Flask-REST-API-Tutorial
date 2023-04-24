from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
#help (Error MSG), required
video_put_args.add_argument("name",type=str, help="Name of the video is req", required = True)
video_put_args.add_argument("views",type=int, help="Views of the video  is req", required = True)
video_put_args.add_argument("likes",type=int, help="Likes of the video  is req", required = True)

# temp Caching
videos = {}

class Video(Resource):
    #Create
    def get(self, videoID):
        return videos[videoID]
    
    #Add Data
    def put(self, videoID):
        args = video_put_args.parse_args()
        videos[videoID] = args
        return videos[videoID], 201

api.add_resource(Video, "/video/<int:videoID>")

    
    
#<> shows params
#api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    #Start App Server and Flask App, With Debug Mode (Log Info)
    app.run(debug=True)