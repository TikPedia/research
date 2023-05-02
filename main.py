#import the libraries
from flask import Flask
from pytrends.request import TrendReq
from pymongo import MongoClient

import json


json_data_list = []
pytrend = TrendReq()
id=0
listTrend = []




trendingtoday = pytrend.trending_searches(pn='france')
trendingtoday = trendingtoday.head(10)

for trend in trendingtoday[0]:
    listTrend.append(trend)
    id += 1


# Data to be written
dictionary = {
    "trendingToday":
        listTrend
}

#print(json.dumps(dictionary))

app = Flask('app')



# ------------- Base de données NoSQL MongoDB

# Variable de la base de données
#PWD : Pt3PoFbQvChsEdZOnSC6
client = MongoClient('containers-us-west-96.railway.app', 7420, username='mongodb', password='Pt3PoFbQvChsEdZOnSC6')
db = client.flask_db
todos = db.todos

# ------------- API FRONT
# Retourne le dictionary à l'url suivant localhost:9000/
@app.route('/')
def run():
    return dictionary

app.run(host='0.0.0.0', port=9000)


