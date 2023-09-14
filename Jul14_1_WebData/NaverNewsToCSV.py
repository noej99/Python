# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# 비정형
# 데이터 자체에 ,가 포함되어 있음
# split하기 어렵기에 csv사용x

f = open("C:/noej/sourceFile/data/csv/naverNews.txt", "a", encoding="utf-8")

con = MongoClient("195.168.9.61")
db = con.xe

for n in db.search_naver_news.find():
    f.write("%s\t" % n["title"])
    f.write("%s\n" % n["description"])

f.close()
con.close()