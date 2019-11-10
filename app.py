from flask import Flask, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo

from resources.news import News

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/kahoot'
#api = Api(app)

#api.add_resource(News, '/newsoutput')
@app.route('/newsoutput')
def test():
	print('ok')
	return 'ok'


def get(country, sources, q, source_from, sortby):
    url = ('https://newsapi.org/v2/everything?'
           'q='+q+'&'
           'from='+source_from+'&'
           'sortBy='+sortby+'&'
           'apiKey=cc2092da085c4fc3897fbb74e2e41ca8')
    return 'ok'
    try:
        response = requests.get(url)
        return r.json, 200
    except:
        return {'message': 'An error occured trying to look up this news'}, 500

if __name__ == '__main__':
    from db import mongo
    mongo.init_app(app)
    app.run(port=5000, debug=True)
