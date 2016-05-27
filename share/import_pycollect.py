#!/usr/bin/env python
from pymongo import MongoClient
import json
import sys
import os


client = MongoClient()
db = client['pycollect']
games = db['games']

with open(sys.argv[1]) as f:
    pycollect = json.load(f)

games.insert_many(pycollect['games'].values())
