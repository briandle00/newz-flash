from flask import Flask, jsonify, request
import requests
from random import randint
from collections import defaultdict

app = Flask(__name__)
#api = Api(app)

#api.add_resource(News, '/newsoutput')
@app.route('/news')
def query():
	if request.args:
		try:
			url = 'https://newsapi.org/v2/everything?'
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
			response = requests.get(url)
			return response.json(), 200
		except:
			return "Error loading response", 500
	else:
		return "No queries received", 200

@app.route('/generate')
def generate():
	# try:
	url = 'https://newsapi.org/v2/top-headlines?'
	url += 'sortBy=popularity&'
	url += 'language=en&'
	url += 'apiKey=2ca567cb295449ecb7277f38e38cb7dd'
	response = requests.get(url)

	source = response.json()['articles'][randint(0, len(response.json()['articles']) - 1)]['source']
	author = response.json()['articles'][randint(0, len(response.json()['articles']) - 1)]['author']
	urlToImage = response.json()['articles'][randint(0, len(response.json()['articles']) - 1)]['urlToImage']
	source = response.json()['articles'][randint(0, len(response.json()['articles']) - 1)]['source']
	titleCorpus = defaultdict(list)
	for i in response.json()['articles']:
		title = i['title'].split()
		for j in range(len(title) - 1):
			titleCorpus[title[j]].append(title[j+1])
		titleCorpus[title[-1]].append('')
	descCorpus = defaultdict(list)
	for i in response.json()['articles']:
		desc = i['description'].split()
		for j in range(len(desc) - 1):
			descCorpus[desc[j]].append(desc[j+1])
		descCorpus[desc[-1]].append('')
	titleKey = list(titleCorpus.keys())[randint(0, len(titleCorpus))]
	descKey = list(descCorpus.keys())[randint(0, len(descCorpus))]
	title = ''
	desc = ''
	while True:
		title += titleKey + " "
		index = randint(0,len(titleCorpus[titleKey]))
		if titleCorpus[titleKey] == []:
			break
		save = titleCorpus[titleKey][index - 1]
		titleKey = save
		if descKey == "":
			break
	while True:
		desc += descKey + " "
		index = randint(0,len(descCorpus[descKey]))
		if descCorpus[descKey] == []:
			break
		descKey = descCorpus[descKey][index - 1]
		if descKey == "":
			break
	to_return = {
		'source': source,
		'author': author,
		'title': title,
		'description': desc,
		'urlToImage': urlToImage,
	}
	return jsonify(to_return)
	# except:
	# 	return "Error generating article", 500

if __name__ == '__main__':
    app.run()