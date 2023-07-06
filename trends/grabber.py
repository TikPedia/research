#!/usr/bin/env python3
from pytrends.request import TrendReq
from pymongo import MongoClient
from datetime import datetime as Date

country = 'france'


def get_trends():
    pytrend = TrendReq()
    trendingtoday = pytrend.trending_searches(pn=country)
    trendingtoday = trendingtoday.head(10)
    listTrend = list(trendingtoday[0])
    # Data to be written
    return  {
        "time": Date.now(),
        "keyword" : listTrend
    }

trend = get_trends()
print(trend)
client = MongoClient("localhost", port=27017, username='root', password='root')
db = client['trends']
db.trends.insert_one(trend)