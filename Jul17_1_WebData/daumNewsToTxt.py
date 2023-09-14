# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

f = open("C:/noej/sourceFile/data/csv/daumNews.txt","a", encoding="utf-8")
con = MongoClient("195.168.9.61")
db = con.xe

for n in db.daumNews.find():
    f.write(n["news"] + "\n")
    
con.close()
f.close()