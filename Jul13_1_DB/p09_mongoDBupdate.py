# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("195.168.9.61")
db = con.xe # con.db명

n = input("이름 : ")
p = int(input("가격 : "))

w = {"name" : n}
s = {"$set" : {"price" : p}}

result = db.jul13_coffee.update_many(w, s)

if result.modified_count >= 1:
    print("성공")

con.close()
