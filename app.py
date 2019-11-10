from flask import Flask, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo

from resources.news import QuestionCreator, Question, QuestionList

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/kahoot'
api = Api(app)

api.add_resource(NewsCreator, '/createnews')


if __name__ == '__main__':
    from db import mongo
    mongo.init_app(app)
    app.run(port=5000, debug=True)