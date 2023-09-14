# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("195.168.9.61")
db = con.xe # con.db명

result = db.jul13_coffee.find()

for c in result:
    print(c["name"], c["cate"], c["price"])

con.close()
