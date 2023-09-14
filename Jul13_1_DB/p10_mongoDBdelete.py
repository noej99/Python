# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("195.168.9.61")
db = con.xe # con.db명

n = input("이름 : ")

w = {"name" : {"$regex" : n}}

result = db.jul13_coffee.delete_many(w)

if result.deleted_count >= 1:
    print("성공")

con.close()
