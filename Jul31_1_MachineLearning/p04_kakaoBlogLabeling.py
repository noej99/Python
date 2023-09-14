# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# 카카오블로그 글 출력
con = MongoClient("195.168.9.61")
db = con.xe
for b in db.kakao_blog.find():
    print(b["blogname"] + "-----")
    print(b["title"])
    print(b["contents"])
    what = input("뭐 : ") # 정상/광고인지 입력받기
    db.kakao_blog.update_one({"_id":b["_id"]}, {"$set":{"what":what}})
con.close()