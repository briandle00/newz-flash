from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
#api = Api(app)

#api.add_resource(News, '/newsoutput')
@app.route('/news')
def query():
	if request.args:
		try:
			url = 'https://newsapi.org/v2/top-headlines?'
			if 'q' in request.args:
				url += 'q='+request.args['q']+'&'
			if 'from' in request.args:
				url += 'from='+request.args['from']+'&'
			if 'to' in request.args:
				url += 'to='+request.args['to']+'&'
			if 'country' in request.args:
				url += 'country='+request.args['country']+'&'
			url += 'sortBy=popularity&'
			url += 'language=en&'
			url += 'apiKey=2ca567cb295449ecb7277f38e38cb7dd'
			# url = ['htps://newsapi.org/v2/top-headlines?',
			#        'country=us&',
			#        'apiKey=2ca567cb295449ecb7277f38e38cb7dd']
			# url = tuple(url)
			# url = ('https://newsapi.org/v2/top-headlines?'
			# 	   'country=us&'
			# 	   'apiKey=2ca567tcb295449ecb7277f38e38cb7dd')
			response = requests.get(url)
			return response.json(), 200
		except:
			return "Error loading response", 500
	else:
		return "No queries received", 200

if __name__ == '__main__':
    app.run()