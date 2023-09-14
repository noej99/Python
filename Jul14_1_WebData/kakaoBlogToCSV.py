# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("195.168.9.61")
db = con.xe

f = open("C:/noej/sourceFile//data/csv/kakaoBlog.txt", "a", encoding="utf-8")
 
for b in db.kakao_blog.find():
    f.write("%s\t" % b["title"])
    f.write("%s\t" % b["contents"])
    f.write("%s\n" % b["blogname"])

con.close()
f.close()