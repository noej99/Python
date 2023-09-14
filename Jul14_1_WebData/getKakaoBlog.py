# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads
from pymongo.mongo_client import MongoClient

def clean(s):
    s = s.replace("<b>", "").replace("</b>", "")
    return s
#################################
# 요청헤더
# h = {"헤더명" : "값", "헤더명" : "값", ...}
h = {"Authorization" : "KakaoAK 5ab3f6c958807e1fa13b50555c88d2c3"}

q = quote("맛집") #  URL인코딩

huc = HTTPSConnection("dapi.kakao.com")
huc.request("GET", "/v2/search/blog?query=" + q, headers=h)
resBody = huc.getresponse().read()

con = MongoClient("195.168.9.61")

db = con.xe

d = loads(resBody)

for b in d["documents"]:
    # db.kakao_blog.insert_one(b)
    # JS객체 형태로(Python dict형태로)
    data = {
        "title":clean(b["title"]),
        "contents":clean(b["contents"]),
        "blogname":clean(b["blogname"])
        }
    # db.테이블명.insert_one(JS객체)
    db.kakao_blog.insert_one(data)

con.close()
huc.close()





