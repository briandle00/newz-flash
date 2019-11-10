from flask import Flask, jsonify, request, render_template
import requests
from random import randint
from collections import defaultdict

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/news')
def query():
	if request.args:
		url = 'https://newsapi.org/v2/top-headlines?'
		if 'q' in request.args:
			url += 'q='+request.args['q']+'&'
		if 'country' in request.args:
			url += 'country='+request.args['country']+'&'
		if 'sortBy' in request.args:
			url += 'sortBy='+request.args['sortBy']+'&'
		else:
			url += 'sortBy=popularity&'
		if 'category' in request.args:
			url += 'category='+request.args['category']+'&'
		url += 'language=en&'
		url += 'apiKey=1db5583f97554370a6d3852ae5ddf700'
		response = dict(requests.get(url).json())
		return render_template('news.html', response=response)
	else:
		return "No queries received", 200

@app.route('/generate')
def generate():
	#try:
	url =  'https://newsapi.org/v2/top-headlines?'
	url += 'sortBy=popularity&'
	url += 'language=en&'
	url += 'apiKey=1db5583f97554370a6d3852ae5ddf700'
	response = requests.get(url)

	source = response.json()['articles'][randint(0, len(response.json()['articles']) - 1)]['source']
	author = response.json()['articles'][randint(0, len(response.json()['articles']) - 1)]['author']
	urlToImage = response.json()['articles'][randint(0, len(response.json()['articles']) - 1)]['urlToImage']
	source = response.json()['articles'][randint(0, len(response.json()['articles']) - 1)]['source']
	titleCorpus = defaultdict(list)
	for i in response.json()['articles']:
		try:
			title = i['title'].split()
			if title != []:
				for j in range(len(title) - 1):
					titleCorpus[title[j]].append(title[j+1])
				titleCorpus[title[-1]].append('')
		except:
			pass
	descCorpus = defaultdict(list)
	for i in response.json()['articles']:
		try:
			desc = i['description'].split()
			if desc != []:
				for j in range(len(desc) - 1):
					descCorpus[desc[j]].append(desc[j+1])
				descCorpus[desc[-1]].append('')
		except:
			pass
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
	response = {
		'source': source,
		'author': author,
		'title': title,
		'description': desc,
		'urlToImage': urlToImage,
	}
	return render_template('generator.html', i=response)
	#except:
	 	#return "Error generating article", 500

if __name__ == '__main__':
    app.run()
