from flask_restful import Resource, reqparse
from bson import json_util
from bson.objectid import ObjectId
from db import mongo

import requests

import datetime
import traceback
import random


class News(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('country',
    #                     type=str,
    #                     required=True,
    #                     help="country field cannot be left bank!"
    #                     )
    # parser.add_argument('sources',
    #                     type=str,
    #                     required=True,
    #                     help="sources field cannot be left bank!"
    #                     )
    # parser.add_argument('q',
    #                     type=str,
    #                     required=True,
    #                     help="q field cannot be left bank!"
    #                     )
    # parser.add_argument('from',
    #                     type=str,
    #                     required=True,
    #                     help="from field cannot be left bank!"
    #                     )
    # parser.add_argument('sortBy',
    #                     type=str,
    #                     required=True,
    #                     help="sortBy field cannot be left bank!"
    #                     )

    def get(self, country, sources, q, source_from, sortby):
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