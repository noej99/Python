# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient

# 로그인해야 하면?
# JS로 동적으로 추가되는거면?
# 웹브라우저 접근만 허용, 프로그램으로 요청막았으면?
# -> 셀레늄(웹브라우저 매크로)

huc = HTTPSConnection("news.daum.net")
huc.request("GET", "/")
resBody = huc.getresponse().read()

con = MongoClient("195.168.9.61")
db = con.xe

daumNews = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")
news = daumNews.select(".list_newsissue .link_txt")

for n in news:
    db.daumNews.insert_one({"news" : n.text.strip()})

con.close()
huc.close()