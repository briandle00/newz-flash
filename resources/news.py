from flask_restful import Resource, reqparse
from bson import json_util
from bson.objectid import ObjectId
from db import mongo

import datetime
import traceback
import random


class NewsCreator(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('country',
                        type=str,
                        required=True,
                        help="country field cannot be left bank!"
                        )
    parser.add_argument('sources',
                        type=str,
                        required=True,
                        help="sources field cannot be left bank!"
                        )
    parser.add_argument('query',
                        type=str,
                        required=True,
                        help="query field cannot be left bank!"
                        )
    parser.add_argument('from',
                        type=str,
                        required=True,
                        help="from field cannot be left bank!"
                        )
    parser.add_argument('sortBy',
                        type=str,
                        required=True,
                        help="sortBy field cannot be left bank!"
                        )