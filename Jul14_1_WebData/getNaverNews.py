# -*- coding:utf-8 -*-

from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
from pymongo.mongo_client import MongoClient
from urllib.parse import quote

def clean(s):
    s = s.replace("&apos;", "")
    s = s.replace("&quot;", "")
    s = s.replace("&amp;", "")
    s = s.replace("<b>", "").replace("</b>", "")
    return s
#################################

con = MongoClient("195.168.9.61")
db = con.xe # con.db명

q = quote("주식") # ㅋ -> %2A

# 요청헤더
h = {"X-Naver-Client-Id" :"uihu8KWuSreB0Qs7lVRa",
     "X-Naver-Client-Secret" : "TbzdbMhPCT"}

huc = HTTPSConnection("openapi.naver.com")
huc.request("GET", "/v1/search/news.xml?query=" + q, headers=h)
resBody = huc.getresponse().read()

news = fromstring(resBody).getiterator("item")

for n in news:
    title = clean(n.find("title").text)
    desc = clean(n.find("description").text)
    data = {"title":title, "description":desc}

    db.search_naver_news.insert_one(data)

con.close() 
huc.close()