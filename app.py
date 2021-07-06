from flask import Flask
from flask_restful import Api, Resource
from text_analize import Analyze, Text
from controller import Controller

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

api.add_resource(Controller, '/Controller/')

if __name__ == "__main__":
    app.run(debug=True)